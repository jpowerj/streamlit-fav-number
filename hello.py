import streamlit as st

markdown_elt = st.markdown("Hello")
cool_button = st.button("Click me")
my_color_picker = st.color_picker("Choose a dang color")

st.sidebar.markdown("Look over here!")

with st.sidebar.form("Options"):
    user_name = st.text_input("What's ur name")
    user_fav_number = st.number_input("Fav number?", min_value=1, max_value=5, value=2, step=1)
    user_photo = st.camera_input("What u look like")
    st.form_submit_button("Click to submit")

if user_fav_number:
    st.markdown(f"Hi {user_name}. Yeah, {user_fav_number} is my fav number too")

if user_name:
    markdown_elt.markdown(f"Hello {user_name}")

st.markdown("Have a great day!")