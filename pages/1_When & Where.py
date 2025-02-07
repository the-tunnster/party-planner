import streamlit
import json

streamlit.set_page_config(
    page_title="When & Where",
    page_icon="📅 🗺"
)

# Load JSON Configs
with open("configs/when.json") as config_when, open("configs/where.json") as config_where:
    when = json.load(config_when)
    where = json.load(config_where)

streamlit.markdown("## 📅 When")
streamlit.write(f"""

{when['date']} <br>
{when['time']} <br>
<br>
{when['duration']}
                
""", unsafe_allow_html=True)

streamlit.divider()

streamlit.markdown("## 📍 Where")
streamlit.write(f"""

{where['address_line_1']}, <br>
{where['address_line_2']}, <br>
{where['suburb']}, {where['city']}, <br>
{where['state']} - {where['zip']}

""", unsafe_allow_html=True)

maps_url = f"https://www.google.com/maps/search/?api=1&query={where['latitude']},{where['longitude']}"
streamlit.markdown(f"[Here's a maps link to make it simpler]({maps_url})", unsafe_allow_html=True)