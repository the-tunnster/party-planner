import streamlit
import json

streamlit.set_page_config(
	page_title="When&Where",
	page_icon="📅 🗺",
	layout="wide"
	)

config_file = open("configs/when_where.json")
when_and_where = json.load(config_file)
config_file.close()

when = when_and_where["when"]
where = when_and_where["where"]

streamlit.markdown(f"""
                   
## When.
{when["date"]} <br>
{when["time"]} <br>
{when["duration"]} <br>

---

## Where.
{where["address_line_1"]}, <br>
{where["address_line_2"]}, <br>
{where["suburb"]}, {where["city"]}, <br>
{where["state"]} - {where["zip"]}. <br>
<br>
{where["maps_url"]}
    
""", unsafe_allow_html=True)
