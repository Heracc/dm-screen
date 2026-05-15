import streamlit as st
import json
all_classes = ["Artificer","Barbarian","Bard","Cleric","Druid","Fighter","Monk","Paladin","Ranger","Rogue","Sorcerer","Warlock","Wizard"]
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
        st.text_input("Race", placeholder="Race", label_visibility="hidden", key="race_input")
        st.selectbox("Class", all_classes, placeholder="Class", label_visibility="hidden", index=None, accept_new_options=True, key="class_input")
        st.text_input("Subclass", placeholder="Subclass", label_visibility="hidden", key="subclass_input")
        st.text_input("Background", placeholder="Background", label_visibility="hidden", key="background_input")
        st.space()
        st.number_input("Armor Class", placeholder="Armor Class", label_visibility="hidden", min_value=0, step=1, key="ac_input")
        st.number_input("HP Max", placeholder="HP Max", label_visibility="hidden", min_value=0, step=1, key="hp_max")
        st.number_input("Speed", placeholder="Speed", label_visibility="hidden", min_value=0, step=1, key="speed_input")
        st.markdown("###### Ability Scores")
        with st.containter(horizontal=True):
            st.number_input("STR", placeholder="STR", label_visibility="hidden", min_value=0, step=1, width=100, key="strength_input")
            st.number_input("STR", placeholder="DEX", label_visibility="hidden", min_value=0, step=1, width=100, key="dexterity_input")
            st.number_input("STR", placeholder="CON", label_visibility="hidden", min_value=0, step=1, width=100, key="constitution_input")
        st.form_submit_button('Add Character', on_click=form_callback)