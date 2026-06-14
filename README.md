# 📊 AI Data Analyst

An AI-powered Data Analyst application built using Streamlit, LangChain, Groq LLM, and SQLite.

The application allows users to interact with a company database using natural language queries and receive intelligent insights without writing SQL queries.

---

## 🚀 Features

- Natural Language Database Queries
- AI-Powered SQL Generation
- Interactive Chat Interface
- Employee Analytics Dashboard
- Department-wise Employee Count Visualization
- Salary Analysis
- SQLite Database Integration
- Streamlit Web Application
- Groq LLM Integration using LangChain

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Groq
- SQLite
- Plotly
- Pandas
- Git & GitHub

---

## 📂 Project Structure

AI_DATA_ANALYST/

├── app.py

├── create_database.py

├── check_db.py

├── requirements.txt

├── .gitignore

├── database/

│ └── company.db

└── README.md

---

## 📸 Application Preview

### Dashboard

Displays employee count by department using interactive charts.

### AI Chat Assistant

Users can ask questions like:

- What is the average salary?
- Show employees in HR department.
- Which department has the highest average salary?
- Who earns the highest salary?

The AI automatically converts natural language into SQL queries and retrieves results from the database.

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/sindhu123650/AI-DATA-Analyst.git
```

### Move to Project Folder

```bash
cd AI-DATA-Analyst
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Environment Variable

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

### Run Application

```bash
streamlit run app.py
```

---

### Architecture Diagram 

User
 │
 ▼
Streamlit UI
 │
 ▼
LangChain SQL Agent
 │
 ▼
Groq LLM
 │
 ▼
SQLite Database
 │
 ▼
Query Results
 │
 ▼
Streamlit Dashboard

## 🎯 Sample Questions

- What is the average salary?
- List all employees in HR department.
- Show average salary by department.
- Which department has the highest average salary?
- Show employee count by department.

---

## 👩‍💻 Author

Sindhu K

GitHub:
https://github.com/sindhu123650
