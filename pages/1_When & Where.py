import streamlit

streamlit.set_page_config(
	page_title="When&Where",
	page_icon="📅 🗺",
	layout="wide"
	)

streamlit.markdown("""
				   
## When.
	Day/Month/Year
	HH:MM:00	
	Duration
				   
---

## Where.
	Address Line 1,
	Address Line 2,
	Suburb, City,
	State - Postcode.
				   
	<maps.link.com>
""")
