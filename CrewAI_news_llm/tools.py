#from serper.dev website, create free api key
from dotenv import load_dotenv

load_dotenv()
import os

#API Key Acquisition: Acquire a serper.dev API key at https://serper.dev/

os.environ['SERPER_API_KEY'] = os.getenv("SERPER_API_KEY")

from crewai_tools import SerperDevTool

#initialize tool for internet searching capabilities
tool = SerperDevTool()