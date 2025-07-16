from crewai import Agent, Task
from agents.content_analyzer import content_analyze
from helper import get_llm

class PainAgent:
    """Class for extracting user pain points."""
    def __init__(self):
        self.llm = get_llm()

    def extract_pain_agent(self):
        """Create an agent for extracting user pain points."""
        agent = Agent(
            role="Pain Point Identifier",
            goal=(
                "List the user's main frustrations and pain points as revealed in their Reddit activity. "
                "For each, provide a short, clear statement suitable for a 'Frustrations' section in a persona profile. "
                "Format output as a bulleted list."
            ),
            backstory=(
                "You are a customer experience analyst specializing in frustration and pain point extraction for persona creation. "
                "Your output is concise and formatted for direct inclusion in a persona's Frustrations section."
            ),
            verbose=True,
            llm=self.llm
        )
        return agent

    def extract_pains_task(self):
        """Create a task for extracting user pain points."""
        extract_pains_task = Task(
            description=(
                "From the analyzed content, identify the user's main frustrations and pain points. "
                "For each, provide a short, clear statement. "
                "For each characteristic, cite the specific Reddit post(s) or comment(s) (with quote or permalink) used to extract that information."
                "Format output as a bulleted list for the 'Frustrations' section of a persona profile."
            ),
            expected_output=(
                "A bulleted list of frustrations/pain points, ready for direct use in the 'Frustrations' section of a persona card."
            ),
            agent=self.extract_pain_agent(),
            context=[content_analyze.analyze_content_task()]
        )
        return extract_pains_task

pain_extract = PainAgent()