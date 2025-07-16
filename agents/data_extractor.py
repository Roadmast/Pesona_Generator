from crewai import Agent, Task
from helper import get_llm
from tools.reddit import RedditExtractionTool
from schema import RedditExtractionInput

class DataExtractor:
    """Class for extracting Reddit data."""
    def __init__(self):
        self.llm = get_llm()
        self.input = RedditExtractionInput(username="")
        self.extract_tool = RedditExtractionTool()
    
    def extract_data_agent(self):
        """Create an agent for extracting Reddit data."""
        agent = Agent(
            role="Reddit Content Extractor",
            goal=(
                "Given a Reddit username or profile URL, use the RedditExtractionTool to fetch all available posts and comments for that user. "
                "Output the raw JSON data as returned by the tool."
                f"{self.input.username}"
            ),
            backstory=(
                "You are an automated data extraction specialist for Reddit. You use specialized tools to gather all available user content for downstream analysis."
            ),
            verbose=True,
            tools=[self.extract_tool],
            llm=self.llm
        )
        return agent

    def extract_data_task(self):
        """Create a task for extracting Reddit data."""
        extract_data_task = Task(
            description=(
                "Given a Reddit username or profile URL, use the RedditExtractionTool to fetch all available posts and comments for that user. "
                "Output the raw JSON data as returned by the tool."
            ),
            expected_output="Raw JSON data containing all posts and comments from the Reddit user.",
            agent=self.extract_data_agent()
        )
        return extract_data_task

data_extract = DataExtractor()