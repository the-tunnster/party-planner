import streamlit as st
from sqlalchemy.orm import joinedload
from utilities.db import SessionLocal
from models.user import User
from utilities.util import getAccessControlConfig


class NewUserAccessClosedError(RuntimeError):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

@st.cache_data(ttl=3600)
def get_or_create_user(email: str, given_name: str, family_name: str) -> User:
    db = SessionLocal()
    try:
        user = db.query(User).options(
            joinedload(User.rsvp),
            joinedload(User.foods),
            joinedload(User.liquors),
            joinedload(User.mixers)
        ).filter(User.email == email).first()
        
        if user is None:
            access_control = getAccessControlConfig()
            if not access_control["allow_new_users"]:
                raise NewUserAccessClosedError(str(access_control["new_user_block_message"]))

            user = User(firstname=given_name, lastname=family_name, email=email)
            db.add(user)
            db.commit()
            db.refresh(user)
            # Fetch again to get eager loading
            user = db.query(User).options(
                joinedload(User.rsvp),
                joinedload(User.foods),
                joinedload(User.liquors),
                joinedload(User.mixers)
            ).filter(User.id == user.id).first()
        
        db.expunge(user)
        return user
    finally:
        db.close()
