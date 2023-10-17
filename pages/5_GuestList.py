import streamlit
from database.select import *

streamlit.set_page_config(
	page_title="TheGuestList.",
	layout="wide"
	)

streamlit.markdown("""

<p>
This is the current list of people who have confirmed or at least filled in a RSVP form. <br>
We thank them for their efforts.<br>
<p> 
				   
---

""", unsafe_allow_html=True)

guest_dataFrame = load_data("guests")

streamlit.dataframe(guest_dataFrame,
					hide_index=True,
					use_container_width=True
					)

