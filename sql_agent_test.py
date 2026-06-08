from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_classic.agents import create_sql_agent

load_dotenv()

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
    verbose=True
)

response = agent_executor.invoke(
    {
        "input":
        "what is the average salary?"
    }
)
print(response["output"])