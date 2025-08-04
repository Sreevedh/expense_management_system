import configtest
from backend.db_helper import fetch_expenses_for_date, fetch_expense_summary
from datetime import date


def test_fetch_expense_for_date_valid_date():
    data = fetch_expenses_for_date("2024-08-15")
    assert len(data) == 1
    assert data[0]['amount'] == 10.0
    assert data[0]['category'] == 'Shopping'
    assert data[0]['notes'] == "Bought potatoes"
    # assert data == [{"id":62, "expense_date": date(2024, 8, 15), "amount":10.0, "category":"Shopping", "notes":"Bought potatoes"}]


def test_fetch_expense_for_date_invalid_date():
    data = fetch_expenses_for_date("9999-08-15")
    assert len(data) == 0


def test_fetch_expense_summary_invalid_date():
    data = fetch_expense_summary("9999-08-05", "8978-03-06")
    assert len(data) == 0


def test_fetch_expense_summary_valid_date():
    data = fetch_expense_summary("2024-08-04", "2024-08-05")
    assert len(data) == 5
