import streamlit
from utilities.util import *

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
                   
<p>
Simply sign in, RSVP as you see fit, and I'll see you later! </br>
Or not, idk? <br>
</p>
                   				   				   
""", unsafe_allow_html=True)

col1, col2 = streamlit.columns([1, 1])
col1.link_button(label="Instagram DM", url="https://www.instagram.com/the_tunnster/", icon=":material/chat:")
col2.link_button(label="Call", url="tel:+918767236939", icon=":material/add_call:")