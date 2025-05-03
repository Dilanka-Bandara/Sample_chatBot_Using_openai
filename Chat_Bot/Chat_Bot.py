import openai
import pandas as pd
from openai import OpenAI

# Create OpenAI client (new method)
client = OpenAI(api_key='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')

# Load dataset
df = pd.read_csv('Loan_details.csv')

# Create dataset summary
def create_data_summary(df):
    summary = f"The dataset has {df.shape[0]} rows and {df.shape[1]} columns.\n"
    summary += "Columns:\n"
    for col in df.columns:
        summary += f"- {col} (type: {df[col].dtype})\n"
    return summary

# Chat function
def ai_agent(user_query, df):
    data_context = create_data_summary(df)

    prompt = f"""
You are a data expert AI agent.

You have been provided with this dataset summary:
{data_context}

Now, based on the user's question:
'{user_query}'

Think step-by-step. Assume you can access and analyze the dataset like a Data Scientist would using Pandas.

Give a clear, final answer.
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=500
    )

    answer = response.choices[0].message.content
    return answer

# Chat loop
print("Welcome to Loan Review AI Agent!")
print("You can ask anything about the loan applicants data.")
print("Type 'exit' to quit.")

while True:
    user_input = input("\nYour question: ")
    if user_input.lower() == "exit":
        break
    try:
        response = ai_agent(user_input, df)
        print("\nAI Agent Response:")
        print(response)
    except Exception as e:
        print(f"Error: {e}")
