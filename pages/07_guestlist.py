import streamlit as st

st.set_page_config(layout="wide")
import pandas as pd
from utilities.db import get_db
from utilities.guards import require_rsvp
from models.user import User

st.set_page_config(layout="wide")

require_rsvp()

st.header("Guestlist", anchor=False)
st.write("Here is the current guestlist for the party.")

db = next(get_db())

# Fetch all users and their RSVP data
users = db.query(User).all()

guest_data: list[dict[str, str]] = []
for user in users:
    if user.rsvp:
        guest_data.append({
            "Guest Name": f"{user.firstname} {user.lastname}",
            "RSVP Status": user.rsvp.status
        })

if guest_data:
    df = pd.DataFrame(guest_data)
    
    # Using streamlit dataframe to present the data nicely
    st.dataframe(df, width="stretch", hide_index=True)  # type: ignore
else:
    st.info("No guests have RSVP'd yet!")
