import streamlit as st
from multiapp import MultiApp
from apps import app_heart, app_parkinson, app_thyroid # import your app modules here

app = MultiApp()

def set_bg_hack_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url("https://ghantee.com/wp-content/uploads/2020/07/tree-wallpaper-illustration-fantasy-HD.jpg");
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )
set_bg_hack_url()

st.markdown("""
# Multiple Disease Prediction APP
the Main aim of this app is to predict different diseases at a single place.
""")

# Add all your application here
app.add_app("Heart Disease Prediction", app_heart.main)
app.add_app("Parkinson Disease Prediction", app_parkinson.main)
app.add_app("Thyroid Disease Prediction", app_thyroid.main)
# The main app
app.run()