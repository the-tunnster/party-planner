import streamlit as st
from utilities.util import getAccessControlConfig


def sidebar_login_logout():
    access_control = getAccessControlConfig()

    with st.sidebar:
        if not st.user.is_logged_in:
            if access_control["allow_new_users"]:
                st.warning("You'll need to log in to continue.")
            else:
                st.warning(str(access_control["login_notice"]))
                st.caption("Existing guests can still sign in and manage their RSVP.")

            if st.button("Login with Google", icon=":material/login:", width='stretch'):
                st.login()
        else:
            if st.button("Logout", icon=":material/logout:", width='stretch'):
                st.logout()
