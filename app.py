import streamlit
from utilities.db import init_db
from utilities.auth import sidebar_login_logout

init_db()
sidebar_login_logout()

pages = {
    "": [
        streamlit.Page("./pages/01_home.py", title="Home", icon=":material/home:", default=True),
        streamlit.Page("./pages/02_when_and_where.py", title="When & Where", icon=":material/location_on:"),
        streamlit.Page("./pages/03_house_rules.py", title="Rules", icon=":material/rule:"),
        streamlit.Page("./pages/04_notice_board.py", title="Notice Board", icon=":material/announcement:"),
    ],
    "Information": [
        streamlit.Page("./pages/05_food.py", title="Food"),
        streamlit.Page("./pages/06_booze.py", title="Drinks"),
        streamlit.Page("./pages/07_guestlist.py", title="Guestlist"),
    ],
    "RSVP": [
        streamlit.Page("./pages/08_rsvp.py", title="RSVP")
    ]
}

pg = streamlit.navigation(pages, position="sidebar", expanded=False)
pg.run()