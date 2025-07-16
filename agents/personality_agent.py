from crewai import Agent, Task
from helper import get_llm
from agents.content_analyzer import content_analyze

class PersonalityAgent:
    """Class for extracting user personality traits."""
    def __init__(self):
        self.llm = get_llm()

    def extract_personality_agent(self):
        """Create an agent for extracting user personality traits."""
        agent = Agent(
            role="Personality Profiler",
            goal=(
                "Infer the user's personality traits using common spectrums (e.g., Introvert/Extrovert, Intuitive/Sensing, etc.). "
                "For each spectrum, indicate where the user likely falls and provide a brief explanation. "
                "Format output as a table or labeled spectrum (like: Introvert [■□□□□] Extrovert) for the 'Personality' section of a persona profile."
            ),
            backstory=(
                "You are a personality psychologist skilled at mapping digital behavior to clear, visual trait spectrums. "
                "Your output is concise, structured, and formatted for persona visualization."
            ),
            verbose=True,
            llm=self.llm
        )
        return agent

    def extract_personality_task(self):
        """Create a task for extracting user personality traits."""
        extract_personality_task = Task(
            description=(
                "From the analyzed content, infer the user's personality traits using common spectrums (e.g., Introvert/Extrovert, Intuitive/Sensing, etc.). "
                "For each spectrum, indicate where the user likely falls and provide a brief explanation. "
                "For each characteristic, cite the specific Reddit post(s) or comment(s) (with quote or permalink) used to extract that information."
                "Format output as a table or labeled spectrum for the 'Personality' section of a persona profile."
            ),
            expected_output=(
                "A table or labeled spectrum of personality traits, with brief explanations, formatted for the 'Personality' section of a persona card."
            ),
            agent=self.extract_personality_agent(),
            context=[content_analyze.analyze_content_task()]
        )
        return extract_personality_task

personality_extract = PersonalityAgent()
