from crewai import Crew, Process
from tools import tool
from agents import researcher, news_writer
from tasks import research_task, write_task

crew = Crew(
    agents = [researcher, news_writer],
    tasks = [research_task, write_task],
    process = [Process.sequential] #Optional: Sequential task execution is default
)

#starting the task execution process with enchanced feedback