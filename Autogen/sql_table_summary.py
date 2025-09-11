import pandas as pd
from autogen.agentchat import AssistantAgent
from autogen_ext.tools.code_execution import PythonCodeExecutionTool

# Simulate SQL query outputs
df1 = pd.DataFrame({
    "EmployeeID": [101, 102, 103, 104],
    "Age": [25, 30, None, 45],
    "Salary": [50000, 60000, 55000, None],
    "Department": ["HR", "Engineering", "Marketing", "Engineering"]
})

df2 = pd.DataFrame({
    "ProductID": [201, 202, 203, 204],
    "Price": [20.5, 35.0, None, 50.0],
    "Stock": [100, 150, 200, None],
    "Category": ["Electronics", "Home", "Electronics", "Garden"]
})

df3 = pd.DataFrame({
    "CustomerID": [301, 302, 303, 304],
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "PurchaseAmount": [250.0, None, 300.0, 150.0],
    "Region": ["North", "South", "East", "West"]
})

# Save as CSVs
df1.to_csv("query_output_employees.csv", index=False)
df2.to_csv("query_output_products.csv", index=False)
df3.to_csv("query_output_customers.csv", index=False)

# Define Python tool
python_tool = PythonCodeExecutionTool()

# Create AssistantAgent
multi_sql_summary_agent = AssistantAgent(
    name="MultiSQLSummarizer",
    system_message="You are a data summarization assistant. Use Python to summarize multiple SQL query outputs and generate column statistics and a brief natural language summary with key points",
    tools=[python_tool],
    llm_config={"model": "gpt-4", "temperature": 0.3}
)

# Send summarization instruction
instruction = """
Summarize the datasets in the following CSV files:
1. 'query_output_employees.csv'
2. 'query_output_products.csv'
3. 'query_output_customers.csv'

For each dataset, provide:
- Column-wise statistics (mean, median for numeric columns)
- Count of missing values per column
- Any notable observations
"""

response = multi_sql_summary_agent.initiate_chat(
    message=instruction,
    sender="user"
)

print(response)
