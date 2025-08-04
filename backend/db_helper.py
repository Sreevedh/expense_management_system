import mysql.connector
from contextlib import contextmanager
from logging_setup import setup

logger = setup('db_helper', 'server.log')

@contextmanager
def get_db_cursor(commit = False):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "expense_manager"
    )

    cursor = connection.cursor(dictionary = True)
    yield cursor

    if commit:
        connection.commit()
    print("Closing cursor")
    cursor.close()
    connection.close()
    

def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expense_called with expense_date: {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses where expense_date=%s",(expense_date,))
        expenses = cursor.fetchall()
        return expenses
    

def delete_expenses(expense_date):
    logger.info(f"delete_expense called with expense_date: {expense_date}")
    with get_db_cursor(commit = True) as cursor:
        cursor.execute("DELETE FROM expenses where expense_date=%s",(expense_date,))
        

def insert_expenses(expense_date, amount, category, notes):
    logger.info(f"insert_expense called with expense_date: {expense_date}, amount:{amount}, category:{category}, note:{notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s,%s,%s,%s)",(expense_date, amount, category, notes,))

def fetch_expense_summary(start_date, end_date):
    logger.info(f"fetch_expense_summary called with start-date: {start_date} and end-date:{end_date}")
    with get_db_cursor() as cursor:
        cursor.execute('''
                        SELECT category,sum(amount) as total 
                        from expenses 
                        where expense_date 
                        between %s and %s 
                        group by category;
                       ''', (start_date, end_date))
        aggregated_data = cursor.fetchall()
        return aggregated_data

def fetch_expense_by_month():
    with get_db_cursor() as cursor:
        cursor.execute('''
                        SELECT
                        MONTHNAME(expense_date) AS month_name,
                        SUM(amount) AS total_amount
                        FROM expenses
                        GROUP BY month_name
                        ORDER BY month_name;
                    ''')
        data_by_month = cursor.fetchall()
        return data_by_month


if __name__ == '__main__':
    pass
    # expenses = fetch_expenses_for_date("2024-08-02")
    # print(expenses)
    # insert_expenses("2024-08-01", 100, "Food", "Eat tasty samosa chat")
    # delete_expenses("2024-08-25")
    # print(fetch_expense_summary("2024-08-01", "2024-08-05"))
