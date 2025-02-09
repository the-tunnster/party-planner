import streamlit
import pandas

from utilities.util import *
from utilities.database import *

streamlit.set_page_config(
	page_title="TheGuestList."
	)

hideSidebar()
actualSidebar()

initialiseData()

streamlit.markdown("""

<p>
This is the current list of people who have confirmed or at least filled in a RSVP form. <br>
We thank them for their efforts.<br>
<p> 
				   
---

""", unsafe_allow_html=True)

guest_data = getAllGuestData()
if len(guest_data) == 0:
	streamlit.markdown("No guests have RSVP'd yet.")
	streamlit.stop()


streamlit.header("Guestlist.")

dataFrame = pandas.DataFrame(guest_data).T.reset_index()
dataFrame.rename(columns={"index":"Name"}, inplace=True)
dataFrame = dataFrame[["Name", "status"]]

streamlit.table(dataFrame)

