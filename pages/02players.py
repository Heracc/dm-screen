import streamlit as st
import pandas as pd
from supabase_client import supabase as sb
from decouple import config
import uuid
from sqlalchemy import create_engine, Column, Integer, Text, Uuid, JSON, Computed
from sqlalchemy.orm import Session, DeclarativeBase
from sqlalchemy.pool import NullPool

USER = config("DB_USER")
PASSWORD = config("DB_PASSWORD")
DBNAME = config("DB_NAME")
PORT = config("DB_PORT")
HOST = config("DB_HOST")

DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

def mod_calc(score):
    return (score-10)//2

class Base(DeclarativeBase):
    pass

class Players(Base):
    __tablename__ = "players"

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    user_id = Column(Uuid)
    name = Column(Text, default="")
    race = Column(Text, default="")
    _class = Column(Text, default="")
    subclass = Column(Text, default="")
    background = Column(Text, default="")
    level = Column(Integer, default=1)
    hp = Column(Integer, default=0)
    ac = Column(Integer, default=0)
    speed = Column(Integer, default=0)
    str = Column(Integer, default=3)
    dex = Column(Integer, default=3)
    con = Column(Integer, default=3)
    int = Column(Integer, default=3)
    wis = Column(Integer, default=3)
    cha = Column(Integer, default=3)
    str_mod = Column(Integer, Computed(mod_calc(str), persisted=True))
    dex_mod = Column(Integer, Computed(mod_calc(dex), persisted=True))
    con_mod = Column(Integer, Computed(mod_calc(con), persisted=True))
    int_mod = Column(Integer, Computed(mod_calc(wis), persisted=True))
    wis_mod = Column(Integer, Computed(mod_calc(int), persisted=True))
    cha_mod = Column(Integer, Computed(mod_calc(cha), persisted=True))
    ## AI told me how to make this a list stored in the column
    languages = Column(JSON)


engine = create_engine(DATABASE_URL, poolclass=NullPool)

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

if st.session_state.user == None:
    st.write("You need to sign in to access this page. Go to the profile page using the sidebar.")
    st.stop()

if "players" not in st.session_state:
    st.session_state.players = {}
    
st.title("players")
st.write("data frame will go here, i promise")

try:
    with Session(engine) as connection:
        st.write("Connection successful!")
except Exception as e:
    st.write(f"Failed to connect: {e} \n Stopping app.")
    st.stop()

def add_player():
    player_input = {
        "user_id": st.session_state.user,
        "name": st.session_state.name_input,
        "ac": st.session_state.ac_input,
        "race": st.session_state.race_input,
        "class": st.session_state.class_input,
        "subclass": st.session_state.subclass_input,
        "background": st.session_state.background_input,
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
        st.form_submit_button('Add Character', on_click=add_player)

if st.button("retrieve"):
    with Session(engine) as session:
        df = pd.read_sql_query(session.query(Players).filter(Players.user_id == st.session_state.user).statement, session.connection())
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
        st.dataframe(df)
    st.dataframe(transposed_df)

#AI gave an explantion of how to make the submit button grayed out if the checkbox isnt checked
with st.form("deleter"):   
    st.text_input("Delete a player", placeholder="Type name here...", key="to_delete")
    confirm = st.checkbox("Are you sure?")
    submit = st.form_submit_button("Delete Player", disabled= not confirm)
    
    if confirm:
        st.toast("deleted")
        

if st.button("Delete"):
    st.text_input(f"Type delete to delete {st.session_state.to_delete}", key="confirmation")
    if st.session_state.confirmation == "delete":
        st.toast("deleted")
        with Session(engine) as session:
            st.toast("in the session")
            session.delete(session.query(Players).filter(Players.user_id == st.session_state.user, Players.name == to_delete).all())
            session.commit()