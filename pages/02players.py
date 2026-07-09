import streamlit as st
import pandas as pd
from systems.players_backend import Players, engine
from sqlalchemy import text
from sqlalchemy.orm import Session

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

if st.session_state.user_id == None:
    
    st.write("You need to sign in to access this page. Go to the profile page using the sidebar.")
    st.stop()

if "players" not in st.session_state:
    st.session_state.players = {}
    
st.title("Players")
header = st.container()

try:
    with Session(engine) as connection:
        result = connection.execute(text("SELECT 1")).scalar()
        if result == 1:
            print("Connected to the database successfully.")
except Exception as e:
    st.write(f"Failed to connect: {e} \n Stopping app.")
    st.stop()

def add_player():
    player_input = {
        "user_id": st.session_state.user_id,
        "name": st.session_state.name_input,
        "ac": st.session_state.ac_input,
        "race": st.session_state.race_input,
        "class": st.session_state.class_input,
        "subclass": st.session_state.subclass_input,
        "background": st.session_state.background_input,
        "level": st.session_state.level_input,
        "languages": st.session_state.language_input,
        "hp": st.session_state.hp_input,
        "speed": st.session_state.speed_input,
        "str": st.session_state.strength_input,
        "dex": st.session_state.dex_input,
        "con": st.session_state.con_input,
        "int": st.session_state.int_input,
        "wis": st.session_state.wis_input,
        "cha": st.session_state.cha_input,
    }
    with Session(engine) as session:
        new_player = Players(
            user_id=player_input["user_id"], 
            name=player_input['name'], 
            race=player_input['race'],
            _class=player_input['class'],
            subclass=player_input['subclass'],
            background=player_input['background'],
            level=player_input['level'],
            languages=player_input['languages'],
            hp=player_input['hp'], 
            ac=player_input['ac'],
            speed=player_input['speed'],
            str=player_input['str'],
            dex=player_input['dex'],
            con=player_input['con'],
            int=player_input['int'],
            wis=player_input['wis'],
            cha=player_input['cha']
            )
        session.add(new_player)
        session.commit()

if st.button("Retrieve Players"):
    with Session(engine) as session:
        # AI helped me write the syntax for this line of code. It creates a pandas dataframe object from the SQL result that is returned when you query the players table 
        # using the Supabase
        df = pd.read_sql_query(session.query(Players).filter(Players.user_id == st.session_state.user_id).statement, session.connection())
        df.drop(columns=['id', 'user_id'], inplace=True)
        #AI told me how to use the pandas rename
        df.rename(columns={'_class': 'Class'}, inplace=True)
        df.columns = df.columns.str.title()
        df.set_index("Name", inplace=True)
        # AI told me how to replace _ with spaces
        df.columns = df.columns.str.replace('_', ' ')
        df.columns.values[5:7] = df.columns[5:7].str.upper()
        df.columns.values[8:20] = df.columns[8:20].str.upper()
        df.columns = df.columns.str.replace('MOD', 'Modifier')
        transposed_df = df.T
    header.dataframe(transposed_df)

with st.expander("Add a Player"):
    with st.form("add_player", clear_on_submit=True, enter_to_submit=False):
        st.text_input("Character Name", placeholder="Character Name", key="name_input")
        st.text_input("Race", placeholder="Race", key="race_input")
        st.selectbox("Class", all_classes, placeholder="Class", index=None, accept_new_options=True, key="class_input")
        st.text_input("Subclass", placeholder="Subclass", key="subclass_input")
        st.text_input("Background", placeholder="Background", key="background_input")
        st.number_input("Level", placeholder="Level", min_value=1, max_value=20, step=1, key="level_input")
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
        st.form_submit_button('Add Character', on_click=add_player)

with st.expander("Delete a Player"):
    with st.form("deleter", clear_on_submit=True):   
        st.text_input("Delete a player", placeholder="Type name here...", key="to_delete")
        confirm = st.checkbox("Are you sure?")
        submit = st.form_submit_button("Delete Player")
        if submit and confirm:
            with Session(engine) as session:
                st.toast(f"Player {st.session_state.to_delete} deleted!")

                session.delete(session.query(Players).filter(Players.user_id == st.session_state.user_id, Players.name == st.session_state.to_delete).first())
                session.commit()
        
with st.expander("Update a Player"):
    to_update = st.text_input("Update a player", placeholder="Type name here...", key="to_update")
    
    with Session(engine) as session:
        player_to_update = session.query(Players).filter(Players.user_id == st.session_state.user_id, Players.name == to_update).first()
        if player_to_update is not None:
            curr_stats = {
                "name": player_to_update.name,
                "ac": player_to_update.ac,
                "race": player_to_update.race,
                "class": player_to_update._class,
                "subclass": player_to_update.subclass,
                "background": player_to_update.background,
                "level": player_to_update.level,
                "languages": player_to_update.languages,
                "hp": player_to_update.hp,
                "speed": player_to_update.speed,
                "str": player_to_update.str,
                "dex": player_to_update.dex,
                "con": player_to_update.con,
                "int": player_to_update.int,
                "wis": player_to_update.wis,
                "cha": player_to_update.cha
            }
            
    if player_to_update is not None:
        class_index = all_classes.index(curr_stats["class"]) if curr_stats["class"] in all_classes else 0
        with st.form("updater", clear_on_submit=True):
            st.text_input("Character Name", value=curr_stats["name"], placeholder="Character Name", key="name_update")
            st.text_input("Race", value=curr_stats["race"], placeholder="Race", key="race_update")
            st.selectbox("Class", all_classes, index=class_index, placeholder="Class", index=None, accept_new_options=True, key="class_update")
            st.text_input("Subclass", value=curr_stats["subclass"], placeholder="Subclass", key="subclass_update")
            st.text_input("Background", value=curr_stats["background"], placeholder="Background", key="background_update")
            st.number_input("Level", value=curr_stats["level"], placeholder="Level", min_value=1, max_value=20, step=1, key="level_update")
            st.number_input("Armor Class", value=curr_stats["ac"], placeholder="Armor Class", min_value=0, step=1, key="ac_update")
            st.number_input("HP Max", value=curr_stats["hp"], placeholder="HP Max", min_value=0, step=1, key="hp_update")
            st.number_input("Speed", value=curr_stats["speed"], placeholder="Speed", min_value=0, step=1, key="speed_update")
            st.markdown("###### Ability Scores")
            with st.container(horizontal=True):
                st.number_input("STR", value=curr_stats["str"], placeholder="STR", min_value=3, max_value=30, step=1, width=200, key="strength_update")
                st.number_input("DEX", value=curr_stats["dex"], placeholder="DEX", min_value=3, max_value=30, step=1, width=200, key="dex_update")
                st.number_input("CON", value=curr_stats["con"], placeholder="CON", min_value=3, max_value=30, step=1, width=200, key="con_update")
                st.number_input("INT", value=curr_stats["int"], placeholder="INT", min_value=3, max_value=30, step=1, width=200, key="int_update")
                st.number_input("WIS", value=curr_stats["wis"], placeholder="WIS", min_value=3, max_value=30, step=1, width=200, key="wis_update")
                st.number_input("CHA", value=curr_stats["cha"], placeholder="CHA", min_value=3, max_value=30, step=1, width=200, key="cha_update")
            st.markdown("###### Languages")
            st.multiselect("Select Languages:", all_languages, default=curr_stats["languages"], key="language_update")
            st.form_submit_button('Update Character')