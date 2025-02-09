import pandas
import streamlit

from utilities.util import *
from utilities.database import *

streamlit.set_page_config(
    page_title="Food & Drinks",
    page_icon="🍕🥤"
)

hideSidebar()
actualSidebar()

initialiseData()

streamlit.markdown(
    """
    <p>
    I'm organising food for everyone, plus some booze and mixers.<br>
    However, I doubt it'll be enough booze to cover everyone's needs and wants.
    </p>

    <p>
    Check the table below for what's being brought and by whom.<br>
    You can contribute to the stock when you RSVP, or not—it's up to you.
    </p>
    """,
    unsafe_allow_html=True
)
streamlit.divider()

rsvps_dict = getAllGuestData()
if len(rsvps_dict) == 0:
	streamlit.markdown("No guests have RSVP'd yet.")
	streamlit.stop()

rsvps_df = pandas.DataFrame.from_dict(rsvps_dict, orient="index").reset_index()
rsvps_df.rename(columns={"index": "guest_name"}, inplace=True)
guest_list = rsvps_df.loc[rsvps_df["status"] == "yes", "guest_name"].tolist()

food_dict = getDataFromFile("food")
food_df = pandas.DataFrame.from_dict(food_dict, orient="index").reset_index()
food_df.rename(columns={"index": "guest_name"}, inplace=True)

food_df = food_df[food_df["guest_name"].isin(guest_list)]

liquor_dict = getDataFromFile("liquor")
liquor_df = pandas.DataFrame.from_dict(liquor_dict, orient="index").reset_index()
liquor_df.rename(columns={"index": "guest_name", "liquor_amount":"volume_in_ml"}, inplace=True)
liquor_df = liquor_df[liquor_df["guest_name"].isin(guest_list)]

mixers_dict = getDataFromFile("mixers")
mixers_df = pandas.DataFrame.from_dict(mixers_dict, orient="index").reset_index()
mixers_df.rename(columns={"index":"guest_name", "mixer_amount":"volume_in_ml"}, inplace=True)
mixers_df = mixers_df[mixers_df["guest_name"].isin(guest_list)]

streamlit.markdown("### Food")
streamlit.table(food_df)

streamlit.markdown("### Liquor")
streamlit.table(liquor_df)

streamlit.markdown("### Mixers")
streamlit.table(mixers_df)
