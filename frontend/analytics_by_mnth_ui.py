import streamlit as st
from datetime import datetime
import requests
import pandas as pd


api_url = "http://localhost:8000"

def analytics_month():
    response = requests.get(f"{api_url}/analytics_month")
    response = response.json()

    df = {}
    for data in response:
        month = data['month_name']
        total_amount = data['total_amount']
        df[month] = total_amount
    st.title("Expense by category")
    st.bar_chart(data=df)
    st.table(df)