import pandas
import streamlit

from utility.utility import *

streamlit.set_page_config(
	page_title="RSVP.",
	page_icon=":heavy_check_mark:"
)

streamlit.markdown("""

## Introduction.
				   
This is where you actually RSVP for the party.
Fill in the form as you see fit, and don't feel pressured to volunteer.

If you have already RSVP'd, resubmitting will update your information instead.
				   
""")

guest_name = streamlit.text_input(label="Enter your first name.", placeholder="first_name").lower()

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

liquor_options=["vodka", "rum", "gin", "whiskey", "bourbon", "wine", "teqiula", "brandy/cognac", "none"]	
liquor_preference = streamlit.selectbox(label="What liquor will you drink/bring along?", options=liquor_options)
liquor_amount = streamlit.number_input(label="Volume of liquor you're bringing.", value=0, format="%d")

mixer_options=["coca-cola/thums_up/pepsi", "sprite/7_up", "red_bull", "diet/sugar_free", "none"]
mixer_preference = streamlit.selectbox(label="What mixers will you bring along?", options=mixer_options)
mixer_amount = streamlit.number_input(label="Volume of mixer you're bringing.", value=0, format="%d")

transportation_self = streamlit.selectbox(label="Can you arrange getting to the location?", options=("yes", "no"))
transportation_others = streamlit.number_input(label="If you have your own vehicle, how many people could you bring along, if required?", value=0, format="%d")

status = streamlit.selectbox(label="Are you confirmed to show up or not?", options=("yes", "no", "maybe"))

submitted = streamlit.button("Submit")

if submitted:
	exists = check_exists(guest_name)

	if not exists:
		insert_data("food", [[guest_name, food_item, food_category, vegetarian]])
		insert_data("guests", [[guest_name, status]])
		insert_data("liquor", [[guest_name, liquor_preference, liquor_amount]])
		insert_data("mixers", [[guest_name, mixer_preference, mixer_amount]])
		insert_data("transportation", [[guest_name, transportation_self, transportation_others]])

		streamlit.write("Thanks for the RSVP.")

	else:
		update_data("food", guest_name, [[guest_name, food_item, food_category, vegetarian]])
		update_data("guests", guest_name, [[guest_name, status]])
		update_data("liquor", guest_name, [[guest_name, liquor_preference, liquor_amount]])
		update_data("mixers", guest_name, [[guest_name, mixer_preference, mixer_amount]])
		update_data("transportation", guest_name, [[guest_name, transportation_self, transportation_others]])

		streamlit.write("You have updated your RSVP.")

	
