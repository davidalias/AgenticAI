import os
from dotenv import load_dotenv

load_dotenv()

llm_config = {
    "config_list": [
        {
            "model": "gpt-3.5-turbo", "api_key": os.environ.get("OPEN_API_KEY")
            }
        ]
    }