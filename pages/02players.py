import streamlit as st
import json
if "players" not in st.session_state:
    st.session_state.players = {}
st.title("players")
st.write("data frame will go here, i promise")

def form_callback():
    st.session_state.players[st.session_state.name_input] = {
        "ac": st.session_state.ac_input
    }
    st.write(st.session_state)

with st.expander("Add a Player"):
    with st.form("add_player", clear_on_submit=True, enter_to_submit=False):
        st.text_input("Character Name", placeholder="Character Name", label_visibility="hidden", key="name_input")
        st.text_input("Armor Class", placeholder="Armor Class", label_visibility="hidden", key="ac_input")
        st.form_submit_button('Add Character', on_click=form_callback)