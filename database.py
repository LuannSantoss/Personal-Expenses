from deta import Deta
import os
from dotenv import load_dotenv

with open('C:/Users/luann/Códigos/Projetos/Personal_expenses/.env.txt', 'r') as f:
    for line in f:
        if 'DETA_KEY' in line:
            deta_key = line.split('=')[1].strip()



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