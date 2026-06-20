import streamlit as st
from supabase_client import supabase

col1, col2 = st.columns([1,1])

def sign_up():
    try:
        response = supabase.auth.sign_up(
        {
            "email": f"{st.session_state.su_username_input}@dmscreen.internal",
            "password": st.session_state.su_password_input,
            "options": {
                "data": {"username": st.session_state.su_username_input}
            }
        })
    except Exception as e:
        st.error(f"Sign up failed: {e}")
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
        st.error(f"Sign in failed: {e}")

def sign_out():
    supabase.auth.sign_out()
    st.session_state.user = None

def forgot_pswrd():
    try:
        supabase.auth.reset_password_email(
        'valid.email@supabase.io',
        {'redirect_to':'http://example.com/account/update-password'}
        )
    except Exception as e:
        st.error(f"Reset email failed: {e}")

if st.session_state.user == None:
    st.write("Sign in to access player sheet storage. \n You can use the initiative tracker and creature stats without an account.")
    with col1:
        with st.form("sign_up"):
            st.write("Sign Up")
            st.text_input("Username", key="su_username_input")
            st.text_input("Password; minimum 6 characters", type="password", key="su_password_input")
            st.form_submit_button("Sign Up", on_click=sign_up)
    with col2:
        with st.form("sign_in"):
            st.write("Sign In")
            st.text_input("Username", key="si_username_input")
            st.text_input("Password; minimum 6 characters", type="password", key="si_password_input")
            st.form_submit_button("Sign In", on_click=sign_in)
else:
    st.write(f"Welcome back,{st.session_state.si_username_input}")
    st.button("Sign Out", on_click=sign_out)