import streamlit as st
from supabase_client import supabase

header = st.container()
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

@st.dialog("Forgot Password?")
def forgot_pswrd():
    st.write("Enter your username to receive a password reset link.")
    username = st.text_input("Username")
    if st.button("Send Reset Email"):
        if not username:
            st.error("Please enter your username.")
        else:
            try:
                email = f"{username}@dmscreen.internal"
                supabase.auth.reset_password_email(
                    email,
                    {'redirect_to': 'http://dmscreen0.streamlit.app/reset-password'}
                )
                st.success("Password reset email sent! Check your inbox for the reset link.")
            except Exception as e:
                st.error(f"Reset email failed: {e}")
                
                
def otp_submit():
    response = supabase.auth.verify_otp({
    'email': f'{st.session_state.otp_username}@dmscreen.internal',
    'token': f'{st.session_state.otp_code}',
    'type': 'email',
})                


if st.session_state.user == None:
    header.write("Sign in to access player sheet storage. \n You can use the initiative tracker and creature stats without an account.")
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
    if st.button("Forgot Password?"):
        email = st.text_input("Enter your email address to receive a password reset link.")
        response = supabase.auth.sign_in_with_otp({
            'email': 'f{email}',
            'options': {
            'should_create_user': False,
            },
        })
        
        st.write(response)
        with st.form("otp_form"):
            st.text_input("Enter the OTP code sent to your email", key="otp_code")
            st.text_input("Enter username", key="otp_username")
            st.form_submit_button("Submit OTP", on_click=otp_submit)
        
#        st.error("Password reset not made yet.")
#        forgot_pswrd()
else:
    st.write(f"Welcome back,{st.session_state.si_username_input}")
    st.button("Sign Out", on_click=sign_out)
    