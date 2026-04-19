import streamlit
from utilities.util import getConfig

time_and_place = getConfig("when_and_where")

streamlit.header("📅 When", anchor=False)
streamlit.markdown(f"""
<p>
From {time_and_place["when"]['start_time']} {time_and_place["when"]['start_date']} <br>
Till {time_and_place["when"]['end_time']} {time_and_place["when"]['end_date']} <br>
</p>       

<p>
I am going to be there from Friday morning till Sunday evening. <br>
I get that ya'll might be busy or have prior commitments, so feel free to drop by whenever, and for how ever long. <br>
</p>
""", unsafe_allow_html=True)

streamlit.divider()

streamlit.header("📍 Where", anchor=False)
streamlit.markdown(f"""
<p>
{time_and_place["where"]['address_line_1']}, <br>
{time_and_place["where"]['address_line_2']}, <br>
{time_and_place["where"]['suburb']}, {time_and_place["where"]['city']}, <br>
{time_and_place["where"]['state']} - {time_and_place["where"]['zip']}.
</p>               
""", unsafe_allow_html=True)

maps_url = f"https://www.google.com/maps/search/?api=1&query={time_and_place['where']['latitude']},{time_and_place['where']['longitude']}"

# Replace page_link with link_button
streamlit.link_button(
    label="Check on Maps", 
    url=maps_url, 
    width="stretch"
)