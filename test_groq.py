from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase
from langchain_classic.chains import create_sql_query_chain


load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

db = SQLDatabase.from_uri(
    "sqlite:///database/company.db"
)

chain = create_sql_query_chain(
    llm,
    db
)

question = "who earns the highest salary?"

sql_query = chain.invoke(
    {
        "question": question
    }
)

print("Generated SQL Query:")
print(sql_query)

sql_query = sql_query.split("SQLQuery:")[-1].strip()

print("\npure SQL:")
print(sql_query)

result = db.run(sql_query)

print("\nresult:")

print(result)

final_prompt = f"""
you are a Data Analyst.

User Question: {question}

SQL Query :
{sql_query}

Database Result:
{result}

provide a clear natural language answer.
"""

final_response = llm.invoke(final_prompt)

print(final_response.content)
