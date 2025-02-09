import streamlit
import json
import os

def hideSidebar():
	streamlit.markdown("""
		<style>
			[data-testid="stSidebarNav"] {
				display: none !important;
			}
			[data-testid="stSidebarContent"] {
				padding-top: 0px;
			}
		</style>
	""", unsafe_allow_html=True)

def actualSidebar():
	streamlit.sidebar.title("📌 Navigation Shiz")
	streamlit.sidebar.page_link(page="./PartyTime.py", label="🎉 PartyTime.")
	streamlit.sidebar.page_link(page="./pages/when_and_where.py", label="🗓️ Event Deets.")
	streamlit.sidebar.page_link(page="./pages/rsvp.py", label="📝 RSVP.")
	streamlit.sidebar.markdown("---")

	streamlit.sidebar.title("Post RSVP")
	streamlit.sidebar.page_link(page="./pages/rules_and_notices.py", label="📜 Rules & Notices.")
	streamlit.sidebar.page_link(page="./pages/food_and_drinks.py", label="🍕🍺 Food & Booze.")
	streamlit.sidebar.page_link(page="./pages/guestlist.py", label="👥 Guestlist.")

def getConfig(config_name):
	with open(f"configs/{config_name}.json") as config:
		return json.load(config)

def checkFileExists(file_name):
	return os.path.exists(file_name)

def initialiseData():
	if not checkFileExists("data/rsvps.json"):
		with open("data/rsvps.json", "w") as file:
			json.dump({}, file, indent=4)

	if not checkFileExists("data/food.json"):
		with open("data/food.json", "w") as file:
			json.dump({}, file, indent=4)
	
	if not checkFileExists("data/liquor.json"):
		with open("data/liquor.json", "w") as file:
			json.dump({}, file, indent=4)

	if not checkFileExists("data/mixers.json"):
		with open("data/mixers.json", "w") as file:
			json.dump({}, file, indent=4)
