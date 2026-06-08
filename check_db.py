from langchain_community.utilities import SQLDatabase

db = SQLDatabase.from_uri(
    "sqlite://database/company.db"
)




print(db.run("SELECT COUNT(*) FROM Employee"))