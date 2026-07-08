import uuid, os
from sqlalchemy import create_engine, Column, Integer, Text, Uuid, JSON, Computed
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.pool import NullPool

USER = os.environ.get("SUPABASE_USER")
PASSWORD = os.environ.get("SUPABASE_PASSWORD")
DBNAME = os.environ.get("SUPABASE_NAME")
PORT = os.environ.get("SUPABASE_PORT")
HOST = os.environ.get("SUPABASE_HOST")

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
