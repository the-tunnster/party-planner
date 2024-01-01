import streamlit
from database.select import *

streamlit.set_page_config(
    page_title="Food&Drinks",
	page_icon="🍕🥤",
	layout="wide"
)

streamlit.markdown("""

<p>				   
I'm organising food for everyone, and some booze and mixers. <br>   
However, I doubt it'll be enough booze to cover everyone's needs and wants.
<p>

<p>			   
Check the table below for what's being brought and by whom. <br>	   
You can contribute to the stock when you RSVP, or not, it's up to you.
<p>
				   
""", unsafe_allow_html=True)
streamlit.divider()

guest_dataframe = load_data("guests")
guest_list = guest_dataframe[guest_dataframe["confirmed"] == 'yes']["guest_name"].tolist()

food_dataFrame = load_data("food")
food_dataFrame = food_dataFrame[food_dataFrame["guest_name"].isin(guest_list)]

liquor_dataFrame = load_data("liquor")
liquor_dataFrame = liquor_dataFrame[liquor_dataFrame["guest_name"].isin(guest_list)]

mixers_dataFrame = load_data("mixers")
mixers_dataFrame = mixers_dataFrame[mixers_dataFrame["guest_name"].isin(guest_list)]

transportation_dataFrame = load_data("transportation")
transportation_dataFrame = transportation_dataFrame[transportation_dataFrame["guest_name"].isin(guest_list)]

streamlit.markdown("### Food.")
streamlit.dataframe(food_dataFrame,
					hide_index=True,
					use_container_width=True,
					)

streamlit.markdown("### Liquor.")
streamlit.dataframe(liquor_dataFrame,
					hide_index=True,
					use_container_width=True
					) 

streamlit.markdown("### Mixers.")
streamlit.dataframe(mixers_dataFrame,
					hide_index=True,
					use_container_width=True
					)

streamlit.markdown("### Transportation.")
streamlit.dataframe(transportation_dataFrame,
					hide_index=True,
					use_container_width=True
					)
