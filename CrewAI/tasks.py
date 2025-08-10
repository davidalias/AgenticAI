from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

#Research Task
research_task = Task(
    description = (
        "Identify the video {topic}."
        "Get detailed information of the video from the channel."
    ),
    expected_output = 'A comprehensive 3 paragraphs long report based on the {topic} of video content.',
    tools = [yt_tool],
    agent = blog_researcher
)

##Writing task
write_task =(
    description = (
        'get info from the youtube channel on the topic {topic}.'
    ),
    expected_output = "Summarize the info from the youtube channel video on the topic{topic} and create blog content.",
    tools = [yt_tool],
    agent = blog_writer,
    async_execution = True, #since ours is sequential, should be set as False
    output_file = 'new_blog-post.md' #Example of output customization
)