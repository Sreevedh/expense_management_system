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
    git clone
    cd ex
    ```
2. **Install dependencies**
    ```commandline
    pip install -r requirements.txt
    ```
3. **Run the FastApi server**
    ```commandline
    uvicorn server:app --reload
    ```
4. **Run the Streamlit UI**
    ```commandline
    streamlit run app.py
    ```
    