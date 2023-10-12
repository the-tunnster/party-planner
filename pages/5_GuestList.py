import streamlit
from utility.utility import *

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

guest_dataFrame = load_dataset("guests")
#mask = guest_dataFrame["confirmed"] == "yes"

#guest_dataFrame = guest_dataFrame[mask]

streamlit.dataframe(guest_dataFrame,
					hide_index=True,
					use_container_width=True
					)

