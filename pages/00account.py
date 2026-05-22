import streamlit as st
from supabase_client import supabase

def sign_up():
    response = supabase.auth.sign_up(
    {
        "email": f"{st.session_state.su_username_input}@dmscreen.internal",
        "password": st.session_state.su_password_input,
        "options": {
            "data": {"username": st.session_state.su_username_input}
        }
    })
    st.session_state.user = response.user.id

def sign_in():
    try:
        response = supabase.auth.sign_in_with_password(
        {
            "email": f"{st.session_state.si_username_input}@dmscreen.internal",
            "password": st.session_state.si_password_input,
            "options": {
                "data": {"username": st.session_state.si_username_input}
            }
        })
        st.session_state.user = response.user.id
    except Exception as e:
        st.write(f"Login failed: {e}")

def sign_out():
    supabase.auth.sign_out()
    st.session_state.user = None

if st.session_state.user == None:
    st.write("Sign in to access player sheet storage. \n You can use the initiative tracker and bestiary without an account, though :)")
    with st.form("sign_up"):
        st.write("Sign Up")
        st.text_input("Username", key="su_username_input")
        st.text_input("Password; minimum 6 characters", type="password", key="su_password_input")
        st.form_submit_button("Sign Up", on_click=sign_up)
    with st.form("sign_in"):
        st.write("Sign In")
        st.text_input("Email", key="si_username_input")
        st.text_input("Password; minimum 6 characters", type="password", key="si_password_input")
        st.form_submit_button("Sign In", on_click=sign_in)
else:
    st.write("Welcome back!")
    st.write(f"user id: {st.session_state.user}")
    st.button("sign out", on_click=sign_out)
