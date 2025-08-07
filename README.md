# EXPENSE MANAGEMENT SYSTEM

This application gives our daily expenses, built using Streamlit as frontend and a FASTAPI as backend.

## Project Structure
- **frontend** : Streamlit. 
- **backend**: Python.
- **tests**: Contains tests for backend.
- **requirements.txt**: List the required Python packages.
- **README.md**: Information about the project.

1. **Clone Reposistory**
    ```bash
    git clone https://github.com/Sreevedh/expense_management_system.git
    cd expense_management_system
    ```
2. **Download Docker**
3. **Download MySQL Workbench**
   ```
   Required for viewing the data.
   ```
4. **Creating a SQL Connection**
   ```
   1. Create a SQL connection with the following parameters
       host: 127.0.0.1
       password: root
       port: 8080
   
   2. Create a Database named "expense_manager"
       CREATE DATABASE IF NOT EXISTS expense_manager;
       USE expense_manager;
       CREATE TABLE IF NOT EXISTS expenses (
        id INT AUTO_INCREMENT PRIMARY KEY,
        expense_date DATE NOT NULL,
        amount DECIMAL(10, 2) NOT NULL,
        category VARCHAR(50),
        notes TEXT);
       
   ```
5. **Docker compose up**
       ```
       docker compose up
       ```
Once docker compose is up and running go to
http://localhost:8501/   for the UI.
    
