import streamlit as st
from datetime import datetime
import requests

api_url = "http://localhost:8000"

def add_update():
    selected_date = st.date_input("Enter Date:",datetime(2024, 8, 1), label_visibility="collapsed")
    response = requests.get(f"{api_url}/expense/{selected_date}")
    if response.status_code == 200:
        existing_expenses = response.json()
    else:
        st.error("Failed to retrieve expenses")
        existing_expenses = []

    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]
    with st.form(key="expense_form"): #this is used to uniquely identify this form.
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text("Amount")
        with col2:
            st.text("Category")
        with col3:
            st.text("Note")
        
        expenses = []
        for i in range(len(existing_expenses)+2):
            if i < len(existing_expenses):
                amount = float(existing_expenses[i]['amount'])
                category = existing_expenses[i]['category']
                notes = existing_expenses[i]['notes']
            else:
                amount = 0.0
                category = "Shopping"
                notes = ""

            col1, col2, col3 = st.columns(3)
            with col1:
                amount_input = st.number_input("Amount", min_value=0.0, step=1.0, value=amount, key=f"amount_{i}", label_visibility="collapsed")
            with col2:
                category_input = st.selectbox(label="Category", options=categories, index=categories.index(category), key=f"category_{i}", label_visibility="collapsed")
            with col3:
                note_input = st. text_input(label="Notes", value=notes, key=f"notes_{i}", label_visibility="collapsed")

            expenses.append({
                'amount':amount_input,
                'category':category_input,
                'notes':note_input
            })

        submit_button = st.form_submit_button()
        if submit_button:
            filtered_expense = [expense for expense in expenses if expense['amount']>0]
            response = requests.post(f"{api_url}/expense/{selected_date}", json=filtered_expense)
            st.write("Response status:", response.status_code)
            st.write("Response content:", response.text)
            if response.status_code == 200:
                st.success("Expenses updated successfully.")
            else:
                st.error("Failed to update expenses.")

