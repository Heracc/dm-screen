import streamlit as st
from supabase_client import supabase

if "user" not in st.session_state:
    st.session_state.user = None

def sign_up(email, password):
    response = supabase.auth.sign_up(
    {
        "email": email,
        "password": password
    })
    st.write(f"heres the user id: {response[id]}")
    st.session_state.user = response[id]

def sign_in(email, password):
    response = supabase.auth.sign_in_with_password(
    {
        "email": email,
        "password": password
    })
    st.session_state.user = response[id]

def sign_out():
    supabase.auth.sign_out()
    st.session_state.user = None

if st.session_state.user == None:
    st.write("Sign in to access player sheet storage. \n You can use the initiative tracker and bestiary without an account, though :)")
    with st.form("sign_up"):
        st.write("Sign Up")
        su_email_input = st.text_input("Email")
        su_password_input = st.text_input("Password; minimum 6 characters", type="password")
        st.sign_up(su_email_input, su_password_input)
    with st.form("sign_in"):
        st.write("Sign In")
        si_email_input = st.text_input("Email")
        si_password_input = st.text_input("Password; minimum 6 characters", type="password")
        st.sign_up(si_email_input, si_password_input)
else:
    st.write("Welcome back!")
    st.write(f"user id: {st.session_state.user}")
    st.button("sign out", on_click=sign_out)
initiative_page = st.Page("pages/01initiative.py", title="Initative Tracker")
players_page = st.Page("pages/02players.py", title="Players")
bestiary_page = st.Page("pages/03bestiary.py", title="Bestiary")

pg = st.navigation([initiative_page, players_page, bestiary_page])
pg.run()
