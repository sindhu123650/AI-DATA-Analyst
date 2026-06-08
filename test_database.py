from langchain_community.utilities import SQLDatabase

db = SQLDatabase.from_uri(
    "sqlite:///database/company.db"
)

print(db.get_usable_table_names())


print(db.get_table_info())

result = db.run(
    """ 
    SELECT AVG(salary)
    FROM Employee
    """
)

print(result)
