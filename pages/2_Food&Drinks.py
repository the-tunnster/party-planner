import pandas
import streamlit

streamlit.set_page_config(
    page_title="Food&Drinks.",
	page_icon=":pizza: :cup_with_straw:"
)

streamlit.markdown("""

## Intro.
<p>				   
I'm bringing food for everyone, and some booze and mixers. <br>   
However, I doubt it'll be enough booze to cover everyone's needs and wants.
<p>

<p>			   
Check the table below for what's being brought and by whom. <br>	   
You can contribute to the stock when you RSVP, or not, it's up to you.
<p>
				   
""", unsafe_allow_html=True)

food_dataFrame = pandas.read_csv("data/food.csv")
liquor_dataFrame = pandas.read_csv("data/liquor.csv")
mixers_dataFrame = pandas.read_csv("data/mixers.csv")
transportation_dataFrame = pandas.read_csv("data/transportation.csv")

streamlit.markdown("## Food.")
streamlit.table(food_dataFrame)

streamlit.markdown("## Liquor.")
streamlit.table(liquor_dataFrame)

streamlit.markdown("## Mixers.")
streamlit.table(mixers_dataFrame)

streamlit.markdown("## Transportation.")
streamlit.table(transportation_dataFrame)
