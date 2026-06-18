import streamlit as st
import json
import random as rd
from systems.players_backend import Base
from sqlalchemy import Column, Integer, Text, Uuid, JSON

def holder():
    class Encounter(Base):
        __tablename__ = "encounters"

        id = Column(Integer, primary_key=True)
        user_id = Column(Uuid, nullable=False)
        last_updated = Column(Integer, nullable=False)