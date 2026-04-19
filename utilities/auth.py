import streamlit as st


def sidebar_login_logout():
    with st.sidebar:
        if not st.user.is_logged_in:
            st.warning("You'll need to log in to continue.")
            if st.button("Login with Google", icon=":material/login:", width='stretch'):
                st.login()
        else:
            if st.button("Logout", icon=":material/logout:", width='stretch'):
                st.logout()
