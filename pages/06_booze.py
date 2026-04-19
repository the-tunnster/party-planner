import streamlit as st
import pandas as pd
from sqlalchemy.orm import joinedload
from utilities.db import get_db
from utilities.guards import require_rsvp
from models.liqour import Liquor
from models.mixers import Mixer

# Require user to be logged in and have an active RSVP
require_rsvp()

st.title("Booze & Mixers 🍻")
st.write("Check out what everyone is bringing to the party!")

db = next(get_db())

# Let the user choose how they want to see the data
view_mode = st.radio(
    "How would you like to view the list?",
    options=["Summary (Total Quantities)", "Detailed (Who is bringing what)"],
    horizontal=True
)

# Fetch data with users loaded
liquors = db.query(Liquor).options(joinedload(Liquor.user)).all()
mixers = db.query(Mixer).options(joinedload(Mixer.user)).all()

def format_volume(vol_ml: int) -> str:
    if vol_ml >= 1000:
        return f"{vol_ml / 1000:.2f} L".rstrip('0').rstrip('.') if str(vol_ml/1000).endswith("0") else f"{vol_ml / 1000} L"
    return f"{vol_ml} ml"

st.header("Liquor")
if not liquors:
    st.info("No liquor has been offered yet.")
else:
    if view_mode == "Detailed (Who is bringing what)":
        liquor_data = [{
            "Guest": f"{l.user.firstname} {l.user.lastname}" if l.user else "Unknown",
            "Type": l.type,
            "Brand": l.brand,
            "Variant": l.variant,
            "Volume (ml)": l.volume,
            "Volume Format": format_volume(l.volume)
        } for l in liquors]
        df_liquor = pd.DataFrame(liquor_data)[["Guest", "Type", "Brand", "Variant", "Volume Format"]]
        st.dataframe(df_liquor, width='stretch', hide_index=True)
    else:
        # Summary mode
        liquor_data = [{"Type": l.type, "Brand": l.brand, "Variant": l.variant, "Volume": l.volume} for l in liquors]
        df_liquor = pd.DataFrame(liquor_data)
        summary_df = df_liquor.groupby(["Type", "Brand", "Variant"])["Volume"].sum().reset_index()
        summary_df["Total Volume"] = summary_df["Volume"].apply(format_volume)
        st.dataframe(summary_df[["Type", "Brand", "Variant", "Total Volume"]], width='stretch', hide_index=True)

st.header("Mixers")
if not mixers:
    st.info("No mixers have been offered yet.")
else:
    if view_mode == "Detailed (Who is bringing what)":
        mixer_data = [{
            "Guest": f"{m.user.firstname} {m.user.lastname}" if m.user else "Unknown",
            "Type": m.type,
            "Brand/Flavor": m.name,
            "Volume (ml)": m.volume,
            "Volume Format": format_volume(m.volume)
        } for m in mixers]
        df_mixer = pd.DataFrame(mixer_data)[["Guest", "Type", "Brand/Flavor", "Volume Format"]]
        st.dataframe(df_mixer, width='stretch', hide_index=True)
    else:
        # Summary mode
        mixer_data = [{"Type": m.type, "Brand/Flavor": m.name, "Volume": m.volume} for m in mixers]
        df_mixer = pd.DataFrame(mixer_data)
        summary_df = df_mixer.groupby(["Type", "Brand/Flavor"])["Volume"].sum().reset_index()
        summary_df["Total Volume"] = summary_df["Volume"].apply(format_volume)
        st.dataframe(summary_df[["Type", "Brand/Flavor", "Total Volume"]], width="stretch", hide_index=True)
