import streamlit as st

import pandas as pd
from typing import Any, cast

from utilities.db import get_db
from utilities.guards import require_login
from utilities.volume import format_volume_label
from utilities.util import getConfig

from models.user import User
from models.rsvp import RSVP, RSVPDay
from models.food import Food
from models.liqour import Liquor
from models.mixers import Mixer

st.set_page_config(layout="wide")

LIQUOR_VOLUME_OPTIONS = [180, 350, 500, 750, 1000, 1500, 2000]
MIXER_VOLUME_OPTIONS = [250, 300, 600, 750, 1250, 1750, 2000, 2250]
FOOD_TYPE_OPTIONS = ["Vegetarian", "Non-Vegetarian"]

st.title("RSVP for the Party", anchor=False)
current_user = require_login()
st.write(f"Logged in as: **{current_user.firstname} {current_user.lastname} ({current_user.email})**")

# Load Configurations
beverages = getConfig("beverage_lists")
liquors_list = beverages.get("liquors", [])
mixers_list = beverages.get("mixers", [])

when_where = getConfig("when_and_where")
event_days = ["Friday", "Saturday", "Sunday", "Monday"] # Mocked

db = next(get_db())
existing_user = db.query(User).filter(User.id == current_user.id).first()

# Show success message if flag is set
if st.session_state.pop("rsvp_success", False):
    st.success("RSVP Saved Successfully! 🎉")
    st.balloons()

# Default form values
default_status = "Tentative"
default_days = []

if existing_user and existing_user.rsvp:
    default_status = existing_user.rsvp.status
    default_days = [day.day_name for day in existing_user.rsvp.days]
    st.info("You have already RSVP'd! You can update your details below.")

# Hydrate state if not already done
if st.session_state.get("rsvp_hydrated_user") != current_user.email:
    st.session_state["pending_foods"] = [{"type": cast(Food, f).type, "name": cast(Food, f).name, "servings": cast(Food, f).servings} for f in (existing_user.foods if existing_user else [])]  # type: ignore
    st.session_state["pending_liquors"] = [{"type": cast(Liquor, l).type, "brand": cast(Liquor, l).brand, "variant": cast(Liquor, l).variant, "volume": cast(Liquor, l).volume} for l in (existing_user.liquors if existing_user else [])]  # type: ignore
    st.session_state["pending_mixers"] = [{"name": cast(Mixer, m).name, "volume": cast(Mixer, m).volume} for m in (existing_user.mixers if existing_user else [])]  # type: ignore
    st.session_state["rsvp_hydrated_user"] = current_user.email

# --------------------
# Dialogs
# --------------------
@st.dialog("Add a Food Dish")
def add_food_dialog():
    with st.form("add_food_form", clear_on_submit=True, enter_to_submit=False):
        ftype = st.selectbox("Food Type", FOOD_TYPE_OPTIONS)
        fname = st.text_input("Name of Dish")
        fservings = st.number_input("Servings", min_value=1, step=1, value=4)
        if st.form_submit_button("Add Food", width='stretch'):
            if not fname.strip():
                st.error("Please provide a name for the dish.")
            else:
                st.session_state["pending_foods"].append({"type": ftype, "name": fname.strip(), "servings": fservings})
                st.rerun()

@st.dialog("Add Liquor")
def add_liquor_dialog():
    with st.form("add_liquor_form", clear_on_submit=True, enter_to_submit=False):
        ltype = st.selectbox("Liquor Type", liquors_list)
        lbrand = st.text_input("Brand", placeholder="e.g. Absolut")
        lvariant = st.text_input("Variant", value="Standard", placeholder="e.g. Citron")
        lvolume = st.selectbox("Volume", LIQUOR_VOLUME_OPTIONS, format_func=format_volume_label)
        if st.form_submit_button("Add Liquor", width='stretch'):
            if not lbrand.strip():
                st.error("Please provide a brand.")
            else:
                st.session_state["pending_liquors"].append({
                    "type": ltype,
                    "brand": lbrand.strip(),
                    "variant": lvariant.strip() or "Standard",
                    "volume": lvolume
                })
                st.rerun()

@st.dialog("Add Mixer")
def add_mixer_dialog():
    with st.form("add_mixer_form", clear_on_submit=True, enter_to_submit=False):
        mname = st.selectbox("Mixer Name", mixers_list)
        mvolume = st.selectbox("Volume", MIXER_VOLUME_OPTIONS, format_func=format_volume_label)
        if st.form_submit_button("Add Mixer", width='stretch'):
            if not mname:
                st.error("Please provide a name.")
            else:
                st.session_state["pending_mixers"].append({
                    "name": mname, "volume": mvolume
                })
                st.rerun()

# --------------------
# Main Form Layout
# --------------------
st.subheader("Your Attendance", anchor=False)

status = st.radio(
    "Are you coming?",
    options=["Yes", "No", "Tentative"],
    index=["Yes", "No", "Tentative"].index(default_status) if default_status in ["Yes", "No", "Tentative"] else 2,
    label_visibility="collapsed",
)

st.write("Which days will you be attending?")
selected_days: list[str] = []
for day in event_days:
    if st.checkbox(day, value=day in default_days):
        selected_days.append(day)

st.divider()
st.subheader("Contributions (Optional)", anchor=False)

# Food Section
st.markdown("#### Food 🍲")
foods = st.session_state["pending_foods"]
if foods:
    df_food = pd.DataFrame(foods)
    df_food.columns = ["Type", "Name", "Servings"]
    st.dataframe(df_food, width='stretch', hide_index=True)  # type: ignore
    if st.button("Remove Last Food", key="rm_food"):
        st.session_state["pending_foods"].pop()
        st.rerun()
else:
    st.caption("No food contributions added yet.")

if st.button("Add Food Dish", key="btn_add_food", width='stretch'):
    add_food_dialog()

st.divider()

# Liquor Section
st.markdown("#### Liquor 🥃")
liquors = st.session_state["pending_liquors"]
if liquors:
    df_liq = pd.DataFrame(liquors)
    df_liq["Volume"] = df_liq["volume"].apply(format_volume_label)
    df_liq = df_liq[["type", "brand", "variant", "Volume"]]
    df_liq.columns = ["Type", "Brand", "Variant", "Volume"]
    st.dataframe(df_liq, width='stretch', hide_index=True)  # type: ignore
    if st.button("Remove Last Liquor", key="rm_liq"):
        st.session_state["pending_liquors"].pop()
        st.rerun()
else:
    st.caption("No liquor contributions added yet.")

if st.button("Add Liquor", key="btn_add_liq", width='stretch'):
    add_liquor_dialog()

st.divider()

# Mixers Section
st.markdown("#### Mixers 🥤")
mixers = st.session_state["pending_mixers"]
if mixers:
    df_mix = pd.DataFrame(mixers)
    df_mix["Volume"] = df_mix["volume"].apply(format_volume_label)
    df_mix = df_mix[["name", "Volume"]]
    df_mix.columns = ["Mixer Name", "Volume"]
    st.dataframe(df_mix, width='stretch', hide_index=True)  # type: ignore
    if st.button("Remove Last Mixer", key="rm_mix"):
        st.session_state["pending_mixers"].pop()
        st.rerun()
else:
    st.caption("No mixer contributions added yet.")

if st.button("Add Mixer", key="btn_add_mix", width='stretch'):
    add_mixer_dialog()

st.divider()

submitted = st.button("Submit RSVP", width='stretch', type="primary")

if submitted:
    if status in ["Yes", "Tentative"] and not selected_days:
        st.error("Please select at least one day you are attending.")
    else:
        try:
            user = existing_user or db.query(User).filter(User.id == current_user.id).first()
            if user is None:
                raise RuntimeError("Unable to load the logged-in user.")
            user_record = cast(Any, user)
            user_record.firstname = str(current_user.firstname)
            user_record.lastname = str(current_user.lastname)

            if user.rsvp:
                user.rsvp.status = status
                for day in user.rsvp.days:
                    db.delete(day)
            else:
                rsvp = RSVP(user_id=user.id, status=status)
                db.add(rsvp)
                db.commit()
                db.refresh(rsvp)

            if status in ["Yes", "Tentative"]:
                for day_name in selected_days:
                    db.add(RSVPDay(rsvp_id=user.rsvp.id, day_name=day_name))
            elif status == "No":
                for day in user.rsvp.days:
                    db.delete(day)

            for f in user.foods:
                db.delete(f)
            for l in user.liquors:
                db.delete(l)
            for m in user.mixers:
                db.delete(m)

            if status in ["Yes", "Tentative"]:
                for f in foods:
                    db.add(Food(user_id=user.id, type=f["type"], name=f["name"], servings=f["servings"]))
                for l in liquors:
                    db.add(Liquor(user_id=user.id, type=l["type"], brand=l["brand"], variant=l["variant"], volume=l["volume"]))
                for m in mixers:
                    db.add(Mixer(user_id=user.id, name=m["name"], volume=m["volume"]))

            db.commit()
            
            # Refresh the logged-in session user
            from utilities.user_mgmt import get_or_create_user
            get_or_create_user.clear(
                email=str(current_user.email),
                given_name=str(current_user.firstname),
                family_name=str(current_user.lastname),
            )
            st.session_state["user"] = get_or_create_user(
                email=str(current_user.email),
                given_name=str(current_user.firstname),
                family_name=str(current_user.lastname),
            )
            
            st.session_state["rsvp_success"] = True
            st.rerun()
        except Exception as e:
            db.rollback()
            st.error(f"An error occurred: {e}")
