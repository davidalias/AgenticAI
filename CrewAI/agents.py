from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv

load_dotenv()

#Open ai model and key for youtube research
import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "GPT-4o-mini"


#Create senior blog content researcher
blog_researcher = Agent(
    role = "Blog Researcher of Youtube videos"
    goal = "Get relevant video topic{topic} from youtube channel"
    verbose = True,
    memory = True,
    backstory = (
        "Expert in understanding videos in the domain of AI, Data Science, Machine Learning and Generative AI"
    )
    tools = [yt_tool],
    #llm = llm,
    allow_delegation = True #tranfer work of this agent to someone else
)

#Create a senior blog writer agent with YT tool

blog_writer = Agent(
    role = "Blog Writer",
    goal = "Narrate compelling tech stories about the video{topic} from the YT channel",
    verbose = True,
    memory = True,
    backstory =(
        "By simplifying complex topics, you create"
        "engaging narratives that captivate and educate, bringing"
        "new discoveries to light in an accessible manner"
    ),
    tools = [yt_tool],
    #llm = llm,
    allow_delegation = False
)