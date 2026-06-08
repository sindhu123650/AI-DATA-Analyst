import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_classic.agents import create_sql_agent

# ==========================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================

load_dotenv()

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI Data Analyst",
    page_icon="📊",
    layout="wide"
)

# ==========================================
# LOAD AI AGENT
# ==========================================

@st.cache_resource
def load_agent():

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0
    )

    db = SQLDatabase.from_uri(
        "sqlite:///database/company.db"
    )

    toolkit = SQLDatabaseToolkit(
        db=db,
        llm=llm
    )

    agent_executor = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=False
    )

    return agent_executor


agent_executor = load_agent()

# ==========================================
# SESSION STATE
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.title("📊 AI Data Analyst")

    st.success(
        "AI-Powered Database Analytics"
    )

    st.write("✔ Ask questions in plain English")
    st.write("✔ View business analytics")
    st.write("✔ Download employee reports")

    # Download CSV

    conn = sqlite3.connect(
        "database/company.db"
    )

    employee_df = pd.read_sql_query(
        "SELECT * FROM Employee",
        conn
    )

    conn.close()

    csv = employee_df.to_csv(
        index=False
    )

    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name="employees.csv",
        mime="text/csv"
    )

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ==========================================
# TITLE
# ==========================================

st.title("📊 AI Data Analyst")

st.markdown("""
### 🤖 AI-Powered Data Analyst

Ask questions in natural language and get insights from your database instantly.

**Tech Stack:**
- LangChain
- Groq
- SQLite
- Streamlit
- Plotly
""")

# ==========================================
# KPI CARDS
# ==========================================

conn = sqlite3.connect(
    "database/company.db"
)

total_employees = pd.read_sql_query(
    "SELECT COUNT(*) as total FROM Employee",
    conn
)

avg_salary = pd.read_sql_query(
    "SELECT AVG(Salary) as avg_salary FROM Employee",
    conn
)

conn.close()

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Employees",
        int(total_employees["total"][0])
    )

with col2:
    st.metric(
        "Average Salary",
        f"₹{int(avg_salary['avg_salary'][0]):,}"
    )

# ==========================================
# CHART 1
# EMPLOYEE COUNT BY DEPARTMENT
# ==========================================

conn = sqlite3.connect(
    "database/company.db"
)

query1 = """
SELECT
Department,
COUNT(*) as EmployeeCount
FROM Employee
GROUP BY Department
"""

employee_count_df = pd.read_sql_query(
    query1,
    conn
)

conn.close()

fig1 = px.bar(
    employee_count_df,
    x="Department",
    y="EmployeeCount",
    title="Employee Count by Department"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# ==========================================
# CHART 2
# AVG SALARY BY DEPARTMENT
# ==========================================

conn = sqlite3.connect(
    "database/company.db"
)

query2 = """
SELECT
Department,
AVG(Salary) as AvgSalary
FROM Employee
GROUP BY Department
"""

salary_df = pd.read_sql_query(
    query2,
    conn
)

conn.close()

fig2 = px.bar(
    salary_df,
    x="Department",
    y="AvgSalary",
    title="Average Salary by Department"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ==========================================
# CHART 3
# SALARY DISTRIBUTION
# ==========================================

conn = sqlite3.connect(
    "database/company.db"
)

salary_distribution_df = pd.read_sql_query(
    "SELECT Salary FROM Employee",
    conn
)

conn.close()

fig3 = px.histogram(
    salary_distribution_df,
    x="Salary",
    nbins=10,
    title="Salary Distribution"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# ==========================================
# CHAT HISTORY
# ==========================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):
        st.markdown(
            message["content"]
        )

# ==========================================
# CHAT INPUT
# ==========================================

question = st.chat_input(
    "Ask about your database..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.spinner(
        "Analyzing database..."
    ):

        response = agent_executor.invoke(
            {
                "input": question
            }
        )

        answer = response["output"]

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    st.rerun()