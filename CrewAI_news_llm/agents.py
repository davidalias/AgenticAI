from crewai import Agent

from tools import tool

from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

#aistudio.google.com for api key
llm = ChatGoogleGenerativeAI(model = "gemini-1.5-flash",
                             verbose = True,
                             temperature = 0.5,
                             google_api_key = os.getenv("GOOGLE_API_KEY"))

#create senior researcher agent

researcher = Agent(
    role =' Senior Researcher',
    goal = 'Uncover ground-breaking technologies in {topic}',
    verbose = True,
    memory = True,
    backstory = (
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change the world."
    ),
    tools =[tool],
    llm = llm, #if not specified, automatically uses openai model
    allow_delegation = True

)

#Create writer agent with custom tools responsible in writing news blogs

news_writer = Agent(
    role = "Writer",
    goal ="Write compelling tech stories about {topic}",
    verbose = True,
    memory = True,
    backstory = (
        "With a flair of simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner"
    ),
    tools = [tool],
    llm = llm
)