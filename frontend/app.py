import streamlit as st
from add_update_ui import add_update
from analytics_ui import analytics
from analytics_by_mnth_ui import analytics_month


st.title("Expense Management System")

tab1, tab2, tab3 = st.tabs(["Add/Update", "Analytics(Category)", "Analytics(Month)"])
with tab1:
    add_update()
with tab2:
    analytics()
with tab3:
    analytics_month()
