import streamlit
streamlit.set_page_config(
    page_title="Rules&Notices",
	page_icon="⚖",
	layout="wide"
)

streamlit.markdown("""
				   	
## House Rules.  
				   
1. Don't be that guy. If you don't know, someone will let you know.
2. No hard drugs, please.
3. You break it, you at least offer to replace and I'll politely tell you its fine.
				   
---
				   
## Notices and Info.

<p>
There is a theme; <theme_name>. <br>
It is not required to be followed, however, there is a prize for the most accurate. <br>
<p>
				   
""", unsafe_allow_html=True)
