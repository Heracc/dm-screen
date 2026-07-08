import streamlit as st

account_page = st.Page("pages/00account.py", title="Account")
initiative_page = st.Page("pages/01initiative.py", title="Initative Tracker")
players_page = st.Page("pages/02players.py", title="Players")
creatures_page = st.Page("pages/03creatures.py", title="Creatures")

if "user_id" not in st.session_state:
    st.session_state.user_id = None
    st.session_state.username = None

if st.session_state.user_id == None:
    pg = st.navigation([account_page, initiative_page, creatures_page])
else:
    pg = st.navigation([account_page, initiative_page, players_page, creatures_page])
pg.run()
