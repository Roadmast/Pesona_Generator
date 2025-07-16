
from crewai import Agent, Task
from agents.data_extractor import data_extract
from helper import get_llm

llm = get_llm()

class ContentAnalyzer:
    """Class for analyzing Reddit content."""
    def __init__(self):
        self.llm = llm
    
    def analyze_content_agent(self):
        """Create an agent for analyzing Reddit content."""
        agent = Agent(
            role="Content Analyzer",
            goal=(
                "Thoroughly analyze the extracted Reddit user's posts and comments. "
                "Identify key themes, emotional tone, writing style, and recurring topics. "
                "Output a structured summary (JSON) with sections for: main topics, emotional tone, writing style, and notable patterns. "
                "For each characteristic, cite the specific Reddit post(s) or comment(s) (with quote or permalink) used to extract that information."
                "Cite specific posts or comments as evidence for each finding."
            ),
            backstory=(
                "You are an expert in computational linguistics and digital behavior analysis. "
                "You excel at extracting nuanced meaning from user-generated text, providing clear, structured, and evidence-based insights. "
                "Always support your findings with direct quotes or post references."
            ),
            verbose=True,
            llm=self.llm
        )
        return agent

    def analyze_content_task(self):
        """Create a task for analyzing Reddit content."""
        analyze_content_task = Task(
            description=(
                "Analyze the extracted Reddit user data and identify all information needed to build a persona card. "
                "Extract and summarize: Name, Age, Occupation, Status, Location, Tier, Archetype, Motivations, Personality traits, Behaviour & Habits, Frustrations, Goals & Needs, and a key quote. "
                "Format your output as labeled bullet points and short lists for each section, matching the structure of a professional persona profile."
            ),
            expected_output=(
                "A structured summary with the following labeled sections: Name, Age, Occupation, Status, Location, Tier, Archetype, Motivations, Personality, Behaviour & Habits, Frustrations, Goals & Needs, and a key quote. Each section should be ready for direct use in a persona card."
            ),
            agent=self.analyze_content_agent(),
            context=[data_extract.extract_data_task()]
        )
        return analyze_content_task

content_analyze = ContentAnalyzer()
