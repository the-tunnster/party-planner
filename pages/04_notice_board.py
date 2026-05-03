import streamlit

streamlit.set_page_config(layout="wide")

streamlit.header("The Notice Board", anchor=False)
streamlit.markdown("""
<p>
This page is for any notices that I or Dottie want to put up. <br>
This is also where I'll put any updates to the party scene, so check here to stay up to date. <br>
</p>   
""", unsafe_allow_html=True)

streamlit.subheader("The Theme.", anchor=False)   
streamlit.markdown("""
The vibe is mexican, but gang-related. </br>
Baggy sweatpants + wife beaters + bandanas. <br>
I'll bring stick-on temporary tattoos, so be prepared to have your arms shaved. </br>
""", unsafe_allow_html=True)

streamlit.subheader("What I'll be providing.", anchor=False)   
streamlit.markdown("""
- Toothpaste
- Mosquito Repellent
- Shampoo and Shower Gel (If you're particular, bring your own)
- Playing Cards
- A Projector
- A Laptop with a bunch of games and movies                
""", unsafe_allow_html=True)

streamlit.subheader("What you need to bring.", anchor=False)   
streamlit.markdown("""
- Pillow
- Blanket (if you want one, I have some but not a lot)
- Sunglasses
- Towel
- Swimsuit
- A change of clothes
- House slippers or sandals
- Personal toiletries (please bring a toothbrush)
""", unsafe_allow_html=True)

streamlit.subheader("Updates + Changelog", anchor=False)   
streamlit.markdown("""
- 2024-04-20: Added the notice board page.   
- 2024-05-03: Updated the theme.
""", unsafe_allow_html=True)
                                    
                   