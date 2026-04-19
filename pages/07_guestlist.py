import streamlit as st
import pandas as pd
from utilities.db import get_db
from utilities.guards import require_rsvp
from models.user import User

# Require user to be logged in and have an active RSVP
require_rsvp()

st.title("Guestlist 📋")
st.write("Here is the current guestlist for the party.")

db = next(get_db())

# Fetch all users and their RSVP data
users = db.query(User).all()

guest_data = []
for user in users:
    if user.rsvp:
        guest_data.append({
            "Guest Name": f"{user.firstname} {user.lastname}",
            "RSVP Status": user.rsvp.status
        })

if guest_data:
    df = pd.DataFrame(guest_data)
    
    # Using streamlit dataframe to present the data nicely
    st.dataframe(
        df, 
        width="stretch", 
        hide_index=True
    )
else:
    st.info("No guests have RSVP'd yet!")
