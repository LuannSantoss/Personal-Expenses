from deta import Deta
import os
from dotenv import load_dotenv
import streamlit as st

# Load the environment variables
deta_key = st.secrets["deta_key"]


# Initialize with a project key
deta = Deta(deta_key)

# This is how to create/connect a database
db = deta.Base("monthly_reports")


def insert_period(period, incomes, expenses, comment):
    """Returns the report on a successful creation, otherwise raises an error"""
    return db.put({"key": period, "incomes": incomes, "expenses": expenses, "comment": comment})


def fetch_all_periods():
    """Returns a dict of all periods"""
    res = db.fetch()
    return res.items


def get_period(period):
    """If not found, the function will return None"""
    return db.get(period)
