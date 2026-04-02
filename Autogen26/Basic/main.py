from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
import asyncio
import sys
import os
from dotenv import load_dotenv

sys.path.append(os.path.abspath(".."))
load_dotenv()

model_client = OpenAIChatCompletionClient(
    model="gpt-3.5-turbo",
    #api_key="OPENAI_API_KEY",
)

async def get_weather(city: str) -> str:
    """Get the weather for a given city."""
    return f"The weather in {city} is 73 degrees and Sunny."

agent = AssistantAgent(
    name="multi_agent",
    model_client=model_client,
    tools=[get_weather],
    system_message="You are a helpful assistant.",
    reflect_on_tool_use=True,
    model_client_stream=True,  # Enable streaming tokens from the model client.
)

async def main() -> None:
    await Console(agent.run_stream(task="Who is a data scientist?"))
    await model_client.close() # Close the connection to the model client.

if __name__ == "__main__":
    asyncio.run(main())
