from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import streamlit as st

SQLALCHEMY_DATABASE_URL = "sqlite:///./party.db"

@st.cache_resource
def get_engine():
    return create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )

engine = get_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

@st.cache_resource
def init_db():
    # Import all models here to ensure they are registered properly on the metadata
    import models.user                                                  # type: ignore
    import models.rsvp                                                  # type: ignore
    import models.food                                                  # type: ignore
    import models.liqour                                                # type: ignore
    import models.mixers                                                # type: ignore
    
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
