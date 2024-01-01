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
{when["date"]}
{when["time"]}
{when["duration"]}

---

## Where.
{where["address_line_1"]}
{where["address_line_2"]}
{where["suburb"]}, {where["city"]}
{where["state"]} - {where["zip"]}.
	
{where["maps_url"]}
    
""", unsafe_allow_html=True)
