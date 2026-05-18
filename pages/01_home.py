import streamlit
from utilities.util import *

streamlit.set_page_config(layout="wide")

access_control = getAccessControlConfig()

streamlit.title("You've been invited! :tada:", anchor=False)

streamlit.markdown("""

<p>  
I'm throwing a party, and this is just an over-engineered event invitation system. <br>
<p>
				   
<p>	   
All the tabs in the sidebar are self-explanatory. <br> 
If you can't figure it out though, you can hit me up on a call, but I really hope you won't need to. <br>
<p>

<p>
Do remember to check the notice board every now and then, just in case there are any updates. <br>
</p>                   
""", unsafe_allow_html=True)

if access_control["allow_new_users"]:
	streamlit.markdown("""
<p>
Simply sign in, RSVP as you see fit, and I'll see you later! </br>
Or not, idk? <br>
</p>
				   
""", unsafe_allow_html=True)
else:
	streamlit.info("Sign in is currently limited to guests who are already in the system.")
	streamlit.markdown("""
<p>
If you've already been added to the guest list, you can still sign in and submit or update your RSVP. <br>
</p>
				   
""", unsafe_allow_html=True)

streamlit.link_button(label="Call", url="tel:+918767236939", icon=":material/add_call:")