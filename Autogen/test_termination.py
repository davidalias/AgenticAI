import os
from autogen import AssistantAgent, UserProxyAgent, ConversableAgent
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

maddy = ConversableAgent(
    "maddy",
    system_message= "Your name is Maddy and you are part of a duo of comedians",
    llm_config= llm_config,
    human_input_mode="NEVER"
)

joe = ConversableAgent(
    "joe",
    system_message= "Your name is Joe and you are part of a duo of comedians",
    llm_config= llm_config,
    human_input_mode="NEVER"
)

joe.initiate_chat(maddy, message="Maddy, tell me a joke.", max_turns=2)