import streamlit as st
import pandas as pd
from typing import Any

from utilities.guards import require_login
from utilities.db import get_db

from models.food import Food
from models.user import User

current_user = require_login()

st.title("The Feast 🍲", anchor=False)
st.markdown("Here is a look at the menu based on what everyone is bringing!")

db = next(get_db())

# Query all food contributions and join with User to get names
all_foods = db.query(Food).join(User).all()

if not all_foods:
    st.info("The menu is looking a little empty! Go to the RSVP page to add your dishes.")
else:
    food_data = []
    for f in all_foods:
        # PyLance strict typing workaround for relations
        user: Any = f.user
        food_data.append({
            "Contributor": f"{user.firstname} {user.lastname}",
            "Type": f.type,
            "Dish Name": f.name,
            "Servings": f.servings
        })

    df_food = pd.DataFrame(food_data)
    
    # Calculate overarching metrics
    total_servings = df_food["Servings"].sum()
    total_dishes = len(df_food)
    veg_df = df_food[df_food["Type"] == "Vegetarian"]
    veg_servings = veg_df["Servings"].sum() if not veg_df.empty else 0
    nonveg_servings = total_servings - veg_servings

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Dishes", int(total_dishes))
    col2.metric("Total Servings", int(total_servings))
    col3.metric("Veg. Servings", int(veg_servings))
    col4.metric("Non-Veg Servings", int(nonveg_servings))
    
    st.divider()

    # Organized Summary
    st.subheader("Menu by Dish Type", anchor=False)
    summary_df = df_food.groupby(["Type", "Dish Name"])["Servings"].sum().reset_index()
    summary_df = summary_df.sort_values(by=["Type", "Servings"], ascending=[False, False])
    st.dataframe(summary_df, width='stretch', hide_index=True)  # type: ignore

    st.divider()

    # Detailed Overview
    st.subheader("Who is bringing what?", anchor=False)
    detailed_df = df_food[["Contributor", "Type", "Dish Name", "Servings"]]
    st.dataframe(detailed_df, width='stretch', hide_index=True)  # type: ignore

