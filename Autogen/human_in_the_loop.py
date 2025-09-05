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

agent_with_number = ConversableAgent(
    "agent_with_number",
    system_message=(
        "You are playing a game of guess my number. You have the number 58 in your mind"
        "and I will try to guess it. \n"
        "if my guess is much higher than your number, say 'too high'.\n"
        "if my guess is much lower than your number, say 'too low'. \n"
        "if my guess is slightly higher than your number, say 'high'.\n"
        "if my guess is slightly lower than your number, say 'low'. \n"
        "If I guess correctly, say'correct'."
    ),
    llm_config= llm_config,
    is_termination_msg= lambda msg: "58" in msg['content'], #Terminate if correct number is guessed
    human_input_mode="NEVER" #never ask for human input
)

#human in the loop: "NEVER"
agent_guess_number = ConversableAgent(
    "agent_guess_number",
    system_message= (
        "I have a number in my mind, and you will try to guess it."
        "If I say 'too high', you should guess a much lower number."
        "If I say 'high', you should guess a slightly lower number."
        "If I say 'too low', you should guess a much higher number."
        "If I say 'low', you should guess a slightly higher number."
    ),
    llm_config= llm_config,
    human_input_mode="NEVER"
)

#human in the loop: "ALWAYS"
human_proxy = ConversableAgent(
    "human_proxy",
    llm_config=False, #no llm used for human proxy
    human_input_mode="ALWAYS" #always ask for human input
)

#human in the loop: "TERMINATE"
agent_with_number_terminate = ConversableAgent(
    "agent_with_number_terminate",
    system_message=(
        "You are playing a game of guess my number. You have the number 58 in your mind"
        "and I will try to guess it. \n"
        "if my guess is much higher than your number, say 'too high'.\n"
        "if my guess is much lower than your number, say 'too low'. \n"
        "if my guess is slightly higher than your number, say 'high'.\n"
        "if my guess is slightly lower than your number, say 'low'. \n"
        "If I guess correctly, say'correct'."
    ),
    llm_config= llm_config,
    max_consecutive_auto_reply=1,
    is_termination_msg= lambda msg: "58" in msg['content'], #Terminate if correct number is guessed
    human_input_mode="TERMINATE" #after consecutive auto reply, human will be asked whether to exit or continue
)

if __name__ ==  "__main__":

#    agent_with_number.initiate_chat(
#    agent_guess_number,
#    message="I have a number between 1 and 100. Guess it!"
#)
#Start a chat with the agent with an initial guess 
#    result = human_proxy.initiate_chat(
#        agent_with_number,
#        message="10"
#    )

    result = agent_with_number_terminate.initiate_chat(
        agent_guess_number,
        message= "I have a number between 1 and 100. Guess it!"

    )
