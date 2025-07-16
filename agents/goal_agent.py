from crewai import Agent, Task
from helper import get_llm
from agents.content_analyzer import content_analyze

class GoalAgent:
    """Class for extracting user goals and needs."""
    def __init__(self):
        self.llm = get_llm()

    def extract_goal_agent(self):
        """Create an agent for extracting user goals and needs."""
        agent = Agent(
            role="Goal Setter",
            goal=(
                "Identify the user's main goals and needs based on their Reddit activity. "
                "For each, provide a short, actionable statement. "
                "Format output as a bulleted list for the 'Goals & Needs' section of a persona profile."
            ),
            backstory=(
                "You are a life coach and motivational analyst. "
                "You extract actionable goals and needs for direct use in persona design."
            ),
            verbose=True,
            llm=self.llm
        )
        return agent

    def extract_goals_task(self):
        """Create a task for extracting user goals and needs."""
        extract_goals_task = Task(
            description=(
                "From the analyzed content, identify the user's main goals and needs. "
                "For each, provide a short, actionable statement. "
                "For each characteristic, cite the specific Reddit post(s) or comment(s) (with quote or permalink) used to extract that information."
                "Format output as a bulleted list for the 'Goals & Needs' section of a persona profile."
            ),
            expected_output=(
                "A bulleted list of goals and needs, ready for direct use in the 'Goals & Needs' section of a persona card."
            ),
            agent=self.extract_goal_agent(),
            context=[content_analyze.analyze_content_task()]
        )
        return extract_goals_task

goal_extract = GoalAgent()
