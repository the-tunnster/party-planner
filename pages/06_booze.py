from typing import Any
from typing import cast

from sqlalchemy import Column
import streamlit as st

st.set_page_config(layout="wide")
import pandas as pd
from sqlalchemy.orm import joinedload
from utilities.db import get_db
from utilities.guards import require_rsvp
from models.liqour import Liquor
from models.mixers import Mixer

st.set_page_config(layout="wide")

require_rsvp()

st.header("Booze & Mixers", anchor=False)
st.write("Check out what everyone is bringing to the party!")

db = next(get_db())

view_mode = st.radio(
    "How would you like to view the list?",
    options=["Summary (Total Quantities)", "Detailed (Who is bringing what)"],
    horizontal=True
)

# Fetch data with users loaded
liquors = db.query(Liquor).options(joinedload(Liquor.user)).all()
mixers = db.query(Mixer).options(joinedload(Mixer.user)).all()

def format_volume(vol_ml: int | Column[int] | Any) -> str:
    val = cast(int, vol_ml)
    if val >= 1000:
        return f"{val / 1000:.2f} L".rstrip('0').rstrip('.') if str(val/1000).endswith("0") else f"{val / 1000} L"
    return f"{val} ml"

st.header("Liquor")
if not liquors:
    st.info("No liquor has been offered yet.")
else:
    if view_mode == "Detailed (Who is bringing what)":
        liquor_data : list[dict[str, Any]] = []
        for l in liquors:
            liquor_data.append({
                "Guest": f"{l.user.firstname} {l.user.lastname}" if l.user else "Unknown",
                "Type": l.type,
                "Brand": l.brand,
                "Variant": l.variant,
                "Volume (ml)": l.volume,
                "Volume Format": format_volume(l.volume)
            })
        df_liquor = pd.DataFrame(liquor_data)[["Guest", "Type", "Brand", "Variant", "Volume Format"]]
        st.dataframe(df_liquor, width='stretch', hide_index=True) # type: ignore
    else:
        # Summary mode
        liquor_data: list[dict[str, Any]] = [{"Type": l.type, "Brand": l.brand, "Variant": l.variant, "Volume": l.volume} for l in liquors]
        df_liquor = pd.DataFrame(liquor_data)
        summary_df = df_liquor.groupby(["Type", "Brand", "Variant"])["Volume"].sum().reset_index()
        summary_df["Total Volume"] = summary_df["Volume"].apply(format_volume)
        st.dataframe(summary_df[["Type", "Brand", "Variant", "Total Volume"]], width='stretch', hide_index=True) # type: ignore

st.header("Mixers")
if not mixers:
    st.info("No mixers have been offered yet.")
else:
    if view_mode == "Detailed (Who is bringing what)":
        mixer_data : list[dict[str, Any]] = []
        for m in mixers:
            mixer_data.append({
                "Guest": f"{m.user.firstname} {m.user.lastname}" if m.user else "Unknown",
                "Mixer Name": m.name,
                "Volume (ml)": m.volume,
                "Volume Format": format_volume(m.volume)
            })
        df_mixer = pd.DataFrame(mixer_data)[["Guest", "Mixer Name", "Volume Format"]]
        st.dataframe(df_mixer, width='stretch', hide_index=True) # type: ignore
    else:
        # Summary mode
        mixer_data: list[dict[str, Any]] = [{"Mixer Name": m.name, "Volume": m.volume} for m in mixers]
        df_mixer = pd.DataFrame(mixer_data)
        summary_df = df_mixer.groupby(["Mixer Name"])["Volume"].sum().reset_index()
        summary_df["Total Volume"] = summary_df["Volume"].apply(format_volume)
        st.dataframe(summary_df[["Mixer Name", "Total Volume"]], width='stretch', hide_index=True) # type: ignore
