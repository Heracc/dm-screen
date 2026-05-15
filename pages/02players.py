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
        st.number_input("Armor Class", placeholder="Armor Class", min_value=0, step=1, key="ac_input")
        st.number_input("HP Max", placeholder="HP Max", min_value=0, step=1, key="hp_max")
        st.number_input("Speed", placeholder="Speed", min_value=0, step=1, key="speed_input")
        st.markdown("###### Ability Scores")
        st.number_input("STR", placeholder="STR", min_value=0, step=1, width=200, key="strength_input")
        st.number_input("DEX", placeholder="DEX", min_value=0, step=1, width=200, key="dex_input")
        st.number_input("CON", placeholder="CON", min_value=0, step=1, width=200, key="con_input")
        st.number_input("INT", placeholder="INT", min_value=0, step=1, width=200, key="int_input")
        st.number_input("WIS", placeholder="WIS", min_value=0, step=1, width=200, key="wis_input")
        st.number_input("CHA", placeholder="CHA", min_value=0, step=1, width=200, key="cha_input")
        st.form_submit_button('Add Character', on_click=form_callback)