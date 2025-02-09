import streamlit

from utilities.util import *
from utilities.database import *

streamlit.set_page_config(
	page_title="RSVP.",
	page_icon="✔"
)

hideSidebar()
actualSidebar()

initialiseData()

streamlit.markdown(
	"""
	## Introduction.

	<p>	   
	This is where you actually RSVP for the party. <br>
	Fill in the form as you see fit, and don't feel pressured to volunteer. <br>
	The volumes are in millilitres, and you can enter decimals for the mixers, so don't worry about it. <br>
	<p>

	<p>
	If you have already RSVP'd, resubmitting will update your information instead. <br>
	Only the toggled fields will be added, so if you're updating something, only toggle that. <br>
	<p>
	""",
	unsafe_allow_html=True,
)
streamlit.divider()

guest_name = streamlit.text_input(label="Enter the name for the RSVP.", placeholder="first_name last_name").lower().strip()
if guest_name == "":
	streamlit.warning("You cannot proceed without a name.")
	streamlit.stop()

streamlit.divider()

# ------------------------------------------------------------------------------
# 1) Check if guest exists and fetch their data if they do.
# ------------------------------------------------------------------------------
guest_data = getGuestData(guest_name)

guest_data["food_toggle"] = bool(guest_data["food_item"])
guest_data["liquor_toggle"] = bool(guest_data["liquor_preference"])

food_categories = ("snacks", "mains", "dessert")
if guest_data["food_category"] is "":
	default_food_index = 0
else:
	default_food_index = food_categories.index(guest_data["food_category"])

liquor_options = getConfig("liquor")["options"]
mixer_options = getConfig("mixers")["options"]
volumes = [0.0, 60.0, 180.0, 375.0, 750.0, 1000.0]

default_liquor_index = liquor_options.index(guest_data["liquor_preference"])
default_mixer_index = mixer_options.index(guest_data["mixer_preference"])


# ------------------------------------------------------------------------------
# 2) Toggles for food and liquor/mixers.
# ------------------------------------------------------------------------------
col_1, col_2 = streamlit.columns(2)
with col_1:
	streamlit.write("Would you like to bring food?")
	streamlit.write("Would you like to bring liquor & mixers?")

with col_2:
	food = streamlit.toggle(label="F", label_visibility="hidden", value=guest_data["food_toggle"])
	liquor_mixers = streamlit.toggle(label="L", label_visibility="hidden", value=guest_data["liquor_toggle"])

# ------------------------------------------------------------------------------
# 3) Food fields
# ------------------------------------------------------------------------------
col_1, col_2 = streamlit.columns(2)
if food:
	with col_1:
		streamlit.header("Food.")
		food_item = streamlit.text_input(label="What dish will you be bringing?", value=guest_data["food_item"]).lower()
	with col_2:
		streamlit.header("")
		food_category = streamlit.selectbox(label="What category is it?", options=food_categories, index=default_food_index)
else:
	food_item = ""
	food_category = ""

# ------------------------------------------------------------------------------
# 4) Liquor fields
# ------------------------------------------------------------------------------
if liquor_mixers:
	with col_1:
		streamlit.header("Liquor & Mixers.")
		liquor_preference = streamlit.selectbox(
			label="What liquor will you drink/bring along?", options=liquor_options, index=default_liquor_index)
		mixer_preference = streamlit.selectbox(label="What mixers will you bring along?", options=mixer_options, index=default_mixer_index)
	with col_2:
		streamlit.header("")
		liquor_amount = streamlit.selectbox(label="Volume of liquor you're bringing, in ml.", options=volumes, index=volumes.index(guest_data["liquor_amount"]))
		mixer_amount = streamlit.number_input(label="Volume of mixer you're bringing, in ml.", value=guest_data["mixer_amount"],)
else:
	liquor_preference = "none"
	liquor_amount = 0.0
	mixer_preference = "none"
	mixer_amount = 0.0

streamlit.divider()

# ------------------------------------------------------------------------------
# 5) Status
# ------------------------------------------------------------------------------
status_options = ("yes", "no", "maybe")

status = streamlit.selectbox(
	label="Are you sure you're gonna show up? Like hundo p?",
	options=status_options,
	index=status_options.index(guest_data["status"])
)

submitted = streamlit.button("Submit")

# ------------------------------------------------------------------------------
# 6) Final Insert/Update logic
# ------------------------------------------------------------------------------
if submitted:
	exists = checkGuestExists(guest_name)
	if not exists:
		# Insertion workflow
		insertGuestData(
			guest_name,
			food_item,
			food_category,
			liquor_preference,
			liquor_amount,
			mixer_preference,
			mixer_amount,
			status
		)

		if food:
			insertFoodData(guest_name, food_item, food_category)

		if liquor_mixers:
			insertLiquorData(guest_name, liquor_preference, liquor_amount)
			insertMixerData(guest_name, mixer_preference, mixer_amount)

		streamlit.success("Thanks for the RSVP.")
	else:
		# Update workflow
		updateGuestData(
			guest_name,
			food_item,
			food_category,
			liquor_preference,
			liquor_amount,
			mixer_preference,
			mixer_amount,
			status
		)

		if food or guest_data["food_toggle"]:
			updateFoodData(guest_name, food_item, food_category)

		if liquor_mixers or guest_data["liquor_toggle"]:
			updateLiquorData(guest_name, liquor_preference, liquor_amount)
			updateMixerData(guest_name, mixer_preference, mixer_amount)

		streamlit.success("You have updated your RSVP.")
