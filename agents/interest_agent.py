from crewai import Agent, Task
from agents.content_analyzer import content_analyze
from helper import get_llm

class interest_agent:
    """Class for extracting user interests."""
    def __init__(self):
        self.llm = get_llm()

    def extract_interest_agent(self):
        """Create an agent for extracting user interests."""
        agent = Agent(
            role="Interest Extractor",
            goal=(
                "Identify the user's main motivations and interests from their Reddit activity. "
                "For each motivation or interest, provide a short label and a brief supporting explanation. "
                "Format output as a list of motivations/interests with short explanations, suitable for the 'Motivations' section of a persona profile."
            ),
            backstory=(
                "You are a digital psychologist specializing in motivation and interest detection. "
                "Your findings are concise, grouped under 'Motivations', and designed for direct inclusion in a structured persona."
            ),
            verbose=True,
            llm=self.llm
        )
        return agent

    def extract_interests_task(self):
        """Create a task for extracting user interests."""
        extract_interests_task = Task(
            description=(
                "From the analyzed content, extract the user's main motivations and interests. "
                "For each, provide a short label and a brief supporting explanation. "
                "For each characteristic, cite the specific Reddit post(s) or comment(s) (with quote or permalink) used to extract that information."
                "Format output as a labeled list for the 'Motivations' section of a persona profile."
            ),
            expected_output=(
                "A labeled list of motivations/interests with short explanations, suitable for direct inclusion in the 'Motivations' section of a persona card."
            ),
            agent=self.extract_interest_agent() ,
            context=[content_analyze.analyze_content_task()]
        )
        return extract_interests_task

interest_extract = interest_agent()
