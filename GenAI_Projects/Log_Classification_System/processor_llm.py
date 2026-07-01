from dotenv import load_dotenv
from groq import Groq
load_dotenv()

groq_client = Groq()

def classify_with_llm(log_message):

    prompt = f"""
                Classify the log message into one of these categories:
                (1) Workflow Error, (2) Deprecation Warning.
                If you can't figure out a category, return 'Unclassified.
                Only return the category name. No preamble.
                Log message: {log_message}
"""
    chat_completion = groq_client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages = [
            {
                "role":"user",
                "content": prompt
            }
        ]
    )

    return chat_completion.choices[0].message.content

if __name__=="__main__":
    print(classify_with_llm("Lead conversion failed for prospect ID 7842 due to missing contact information."))
    print(classify_with_llm("API endpoint 'getCustomerDetails' is deprecated and will be removed in version 3.2. Use 'fetchCustomerInfo' instead."))
    print(classify_with_llm("System reboot initiated by user 1234."))