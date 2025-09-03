import os
from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv

load_dotenv()

#llm_config = {"config_list": [{"model": "gpt-4", "api_key": os.environ.get("OPEN_API_KEY")}]}

llm_config = {
    "config_list": [
        {
            "model": "gpt-4",
            "api_key": os.getenv("AZURE_OPENAI_API_KEY"),
            "base_url":os.getenv("AZURE_OPENAI_BASE_URL"), #ends with slash, no /deployments
            "api_type": "azure",
            "api_version": "2025-01-01-preview"
        }
    ]
}

assistant = AssistantAgent("assistant", llm_config = llm_config)

user_proxy = UserProxyAgent("user_proxy", code_execution_config= False)

user_proxy.initiate_chat(
    assistant,
    message= "Tell me a joke about data scientists"
)