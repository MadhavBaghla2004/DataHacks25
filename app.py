import streamlit as st
from datetime import datetime

# Set background image using CSS
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://media.wired.com/photos/620eb0f39266d5d11c07b3c5/master/w_2560%2Cc_limit/Gear-Podcast-Gear-1327244548.jpg");
             background-attachment: fixed;
             background-size: cover;
             background-repeat: no-repeat;
             background-position: center;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

# App title
st.title("🎙️ Podcast Virality Predictor")
st.markdown("Use this app to enter podcast episode details. Prediction feature coming soon!")

# Input form
with st.form("episode_form"):
    st.header("Enter Episode Details")

    col1, col2 = st.columns(2)

    with col1:
        podcast_name = st.text_input("Podcast Name")
        title = st.text_input("Episode Title")
        genre = st.text_input("Genre")
        host = st.text_input("Host Name")
        guest = st.text_input("Guest Name")
        date = st.date_input("Date of Upload", datetime.today())
        time = st.time_input("Time of Upload", datetime.now().time())

    with col2:
        length = st.number_input("Length (in minutes)", min_value=1, value=60)
        subscribers = st.number_input("Channel Subscribers", min_value=0, value=100000)
        guest_followers = st.number_input("Guest Followers", min_value=0, value=50000)
        host_followers = st.number_input("Host Followers", min_value=0, value=75000)
        origin = st.text_input("Podcast Origin")
        guest_nat = st.text_input("Guest Nationality")
        host_nat = st.text_input("Host Nationality")
        guest_prof = st.text_input("Guest Profession")

    submitted = st.form_submit_button("Submit")

    if submitted:
        st.success("✅ Your details were submitted! Prediction coming soon.")

