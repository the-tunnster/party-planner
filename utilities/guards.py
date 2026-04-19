import streamlit as st
from models.user import User
from utilities.user_mgmt import get_or_create_user


def require_login() -> User:
    if not st.user.is_logged_in:
        st.session_state["user"] = None
        st.warning("Please log in to access this page.")
        st.stop()
        
    # User is logged in natively
    current_email = str(st.user.email)
    
    # Check if we have the fully featured cached user
    if "user" not in st.session_state or st.session_state["user"] is None or st.session_state["user"].email != current_email:
        st.session_state["user"] = get_or_create_user(
            email=current_email,
            given_name=str(st.user.given_name),
            family_name=str(st.user.family_name),
        )
        
    return st.session_state["user"]


def require_rsvp() -> User:
    """Ensure the user is logged in, and has completed their RSVP."""
    user = require_login()
    
    if not user.rsvp:
        st.warning("You must complete your RSVP before viewing this page.")
        if st.button("Go to RSVP"):
            st.switch_page("pages/08_rsvp.py")
        st.stop()
        
    return user
