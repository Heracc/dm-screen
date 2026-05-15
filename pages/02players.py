import streamlit as st
import json
all_classes = [
    "Artificer","Barbarian","Bard","Cleric","Druid","Fighter","Monk","Paladin","Ranger","Rogue","Sorcerer","Warlock","Wizard"]
all_languages = [
    # Standard Languages
    "Common", 
    "Dwarvish", 
    "Elvish", 
    "Giant", 
    "Gnomish", 
    "Goblin", 
    "Halfling", 
    "Orc",
    
    # Exotic/Rare Languages
    "Abyssal", 
    "Celestial", 
    "Deep Speech", 
    "Draconic", 
    "Infernal", 
    "Primordial", 
    "Sylvan", 
    "Undercommon",
    
    # Secret Languages
    "Druidic", 
    "Thieves' Cant"
]
if "players" not in st.session_state:
    st.session_state.players = {}
st.title("players")
st.write("data frame will go here, i promise")
def mod_calc(score):
    return (score-10)//2

def form_callback():
    st.session_state.players[st.session_state.name_input] = {
        "ac": st.session_state.ac_input,
        "race": st.session_state.race_input,
        "class": st.session_state.class_input,
        "subclass": st.session_state.subclass_input,
        "background": st.session_state.background_input,
        "languages": st.session_state.language_input,
        "maxHitPoints": st.session_state.hp_input,
        "speed": st.session_state.speed_input,
        "modifiers": {
            "str": mod_calc(st.session_state.strength_input),
            "dex": mod_calc(st.session_state.dex_input),
            "con": mod_calc(st.session_state.con_input),
            "int": mod_calc(st.session_state.int_input),
            "wis": mod_calc(st.session_state.wis_input),
            "cha": mod_calc(st.session_state.cha_input),
        },
        "stats": {
            "str": st.session_state.strength_input,
            "dex": st.session_state.dex_input,
            "con": st.session_state.con_input,
            "int": st.session_state.int_input,
            "wis": st.session_state.wis_input,
            "cha": st.session_state.cha_input,
        }

    }
    st.write(st.session_state.players)

with st.expander("Add a Player"):
    with st.form("add_player", clear_on_submit=True, enter_to_submit=False):
        st.text_input("Character Name", placeholder="Character Name", key="name_input")
        st.text_input("Race", placeholder="Race", key="race_input")
        st.selectbox("Class", all_classes, placeholder="Class", index=None, accept_new_options=True, key="class_input")
        st.text_input("Subclass", placeholder="Subclass", key="subclass_input")
        st.text_input("Background", placeholder="Background", key="background_input")
        st.space()
        st.number_input("Armor Class", placeholder="Armor Class", min_value=0, step=1, key="ac_input")
        st.number_input("HP Max", placeholder="HP Max", min_value=0, step=1, key="hp_input")
        st.number_input("Speed", placeholder="Speed", min_value=0, step=1, key="speed_input")
        st.markdown("###### Ability Scores")
        with st.container(horizontal=True):
            st.number_input("STR", placeholder="STR", min_value=3, max_value=30, step=1, width=200, key="strength_input")
            st.number_input("DEX", placeholder="DEX", min_value=3, max_value=30, step=1, width=200, key="dex_input")
            st.number_input("CON", placeholder="CON", min_value=3, max_value=30, step=1, width=200, key="con_input")
            st.number_input("INT", placeholder="INT", min_value=3, max_value=30, step=1, width=200, key="int_input")
            st.number_input("WIS", placeholder="WIS", min_value=3, max_value=30, step=1, width=200, key="wis_input")
            st.number_input("CHA", placeholder="CHA", min_value=3, max_value=30, step=1, width=200, key="cha_input")
        st.markdown("###### Languages")
        st.multiselect("Select Languages:", all_languages, key="language_input")
        st.form_submit_button('Add Character', on_click=form_callback)