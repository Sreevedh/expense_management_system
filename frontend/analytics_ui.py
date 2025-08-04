import streamlit as st
from datetime import datetime
import requests
import pandas as pd

api_url = "http://localhost:8000"

def analytics():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start date", datetime(2024, 8, 1))
    with col2:
        end_date = st.date_input("End_date", datetime(2024, 8, 5))

    if st.button("Get analytics"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        response = requests.post(f"{api_url}/analytics/", json=payload)
        response = response.json()

        data = {
            "Category" : list(response.keys()),
            "Total" : [response[category]["total"] for category in response],
            "Percentage": [response[category]["percent"] for category in response]
        }
        # pd.DataFrame


        table = pd.DataFrame(data)

        df_sorted = table.sort_values(by="Percentage", ascending=False)


        st.title("Expense breakdown by Category")
        st.bar_chart(data=df_sorted.set_index("Category")["Percentage"])
        st.table(df_sorted)


        
        # return response