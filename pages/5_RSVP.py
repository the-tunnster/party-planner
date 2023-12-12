import json
import streamlit

from database.select import *
from database.insert import *
from database.update import *

streamlit.set_page_config(
	page_title="RSVP.",
	page_icon="✔",
	layout="wide"
)

streamlit.markdown("""

## Introduction.

<p>	   
This is where you actually RSVP for the party. <br>
Fill in the form as you see fit, and don't feel pressured to volunteer. <br>
<p>

<p>
If you have already RSVP'd, resubmitting will update your information instead. <br>
Only the toggled fields will be added, so if you're updating somehting, only toggle that. <br>
<p>
				   
""", unsafe_allow_html=True)
streamlit.divider()

guest_name = streamlit.text_input(label="Enter your first and last name.", placeholder="first_name last_name").lower()

streamlit.write("Would you like to bring food?")
food = streamlit.toggle(label="F", label_visibility="hidden")

if food:
	food_item = streamlit.text_input(label="What dish will you be bringing?").lower()
	food_category = streamlit.selectbox(label="What category is it?", options=("snacks", "mains", "dessert"))
	vegetarian = streamlit.selectbox(label="Is it vegetarian?", options=("yes", "no"))
else:
	food_item = None
	food_category = None
	vegetarian = None

streamlit.write("Would you like to bring liquor & mixers?")
liquor_mixers = streamlit.toggle(label="L", label_visibility="hidden")

config_file = open("configs/drinks_mixers.json")
options = json.load(config_file)
config_file.close()

liquor_options = options["liquor"]
mixer_options = options["mixers"]

if liquor_mixers :
	liquor_preference = streamlit.selectbox(label="What liquor will you drink/bring along?", options=liquor_options)
	liquor_amount = streamlit.number_input(label="Volume of liquor you're bringing, in litres.", value=0, format="%d")

	mixer_preference = streamlit.selectbox(label="What mixers will you bring along?", options=mixer_options)
	mixer_amount = streamlit.number_input(label="Volume of mixer you're bringing.", value=0, format="%d")
else:
	liquor_preference = None
	liquor_amount = None

	mixer_preference = None
	mixer_amount = None
	
transportation_self = streamlit.selectbox(label="Can you arrange getting to the location?", options=("yes", "no"))
transportation_others = streamlit.number_input(label="If you have your own vehicle, how many people could you bring along, if required?", value=0, format="%d")

confirmed = streamlit.selectbox(label="Are you confirmed to show up or not?", options=("yes", "no", "maybe"))

submitted = streamlit.button("Submit")

if submitted:
	exists = check_guest_exists(guest_name)

	if not exists:
		insert_data_guests(guest_name, confirmed)
		insert_data_transportation(guest_name, transportation_self, transportation_others)
		if food:
			insert_data_food(guest_name, food_item, food_category, vegetarian)
		if liquor_mixers:
			insert_data_liquor(guest_name, liquor_preference, liquor_amount)
			insert_data_mixers(guest_name, mixer_preference, mixer_amount)

		streamlit.success("Thanks for the RSVP.")

	else:
		update_data_guests(guest_name, confirmed)
		update_data_transportation(guest_name, transportation_self, transportation_others)
		if food:
			update_data_food(guest_name, food_item, food_category, vegetarian)
		if liquor_mixers:
			update_data_liquor(guest_name, liquor_preference, liquor_amount)
			update_data_mixers(guest_name, mixer_preference, mixer_amount)

		streamlit.success("You have updated your RSVP.")

	
