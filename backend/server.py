from fastapi import FastAPI, HTTPException
from datetime import date
from db_helper import fetch_expenses_for_date, insert_expenses, delete_expenses, fetch_expense_summary, fetch_expense_by_month
from typing import List
from pydantic import BaseModel

class Expenses(BaseModel):
    amount: float
    category: str
    notes: str
    # expense_date: date ---> this is not needed in the "response model" so we omit this.

class Date_Range(BaseModel):
    start_date : date
    end_date : date


app =FastAPI()

@app.get("/expense/{expense_date}", response_model= List[Expenses])
def get_expenses(expense_date : date):
    expenses = fetch_expenses_for_date(expense_date)
    if expenses is None:
        raise HTTPException(status_code=500, detail="Fail to retrieve expense summary from database.")
    return expenses


@app.post("/expense/{expense_date}")
def add_or_update_expenses(expense_date: date, expenses : List[Expenses]): # here expenses is the input
    delete_expenses(expense_date)
    for expense in expenses:
        insert_expenses(expense_date, expense.amount, expense.category, expense.notes)
    return {"message": "Expenses uploaded successfully."}


@app.post("/analytics/")
def get_analytics(date_range: Date_Range):
    response = fetch_expense_summary(date_range.start_date, date_range.end_date)
    if response is None:
        raise HTTPException(status_code=500, detail="Fail to retrieve expense summary from database.")
    
    breakdown = {}
    total = sum([row['total']for row in response])
    for row in response:
        percent_each_category = (row['total']/total)*100 if total !=0 else 0
        percent_each_category = round(percent_each_category, 2)
        # row['percent'] = round(percent_each_category,2)
        breakdown[row['category']] = {
            "total": row['total'],
            "percent": percent_each_category
        }

    return breakdown

@app.get("/analytics_month")
def analytics_by_month():
    response = fetch_expense_by_month()
    return response