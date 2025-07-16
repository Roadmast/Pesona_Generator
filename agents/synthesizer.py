from crewai import Agent, Task
from agents.content_analyzer import content_analyze
from agents.interest_agent import interest_extract
from agents.personality_agent import personality_extract
from agents.pain_agent import pain_extract
from agents.goal_agent import goal_extract
from helper import get_llm

class SynthesizerAgent:
    """Class for synthesizing user data."""
    def __init__(self):
        self.llm = get_llm()

    def extract_synthesizer_agent(self):
        """Create an agent for synthesizing user data."""
        agent = Agent(
            role="Persona Synthesizer",
            goal=(
                "Combine all agent outputs into a single, visually organized persona profile. "
                "Format the output to include the following clearly labeled sections: Name, Age, Occupation, Status, Location, Tier, Archetype, Motivations (with short explanations), Personality (trait spectrums or table), Behaviour & Habits (bulleted list), Frustrations (bulleted list), Goals & Needs (bulleted list), and a key quote or summary statement. "
                "Ensure the result is ready for direct use in UX or marketing, matching the style of a professional persona card."
            ),
            backstory=(
                "You are a persona designer. Your job is to assemble structured, visually clear, and actionable persona profiles for design teams. "
                "Your output is always organized by the required sections and easy to read."
            ),
            verbose=True,
            llm=self.llm
        )
        return agent

    def synthesize_persona_task(self):
        """Create a task for synthesizing user data."""
        synthesize_persona_task = Task(
            description=(
                "Combine all previous outputs into a single, visually organized persona profile. "
                "Format the output to include these clearly labeled sections: Name, Age, Occupation, Status, Location, Tier, Archetype, Motivations (with short explanations), Personality (trait spectrums or table), Behaviour & Habits (bulleted list), Frustrations (bulleted list), Goals & Needs (bulleted list), and a key quote or summary statement. "
                "For each characteristic, cite the specific Reddit post(s) or comment(s) (with quote or permalink) used to extract that information."
                "Ensure the result is ready for direct use in UX or marketing, matching the style of a professional persona card."
            ),
            expected_output=(
                "A single formatted persona profile with all required sections, clearly labeled and visually organized for direct use in design or research."
            ),
            agent=self.extract_synthesizer_agent(),
            context=[content_analyze.analyze_content_task(), interest_extract.extract_interests_task(), personality_extract.extract_personality_task(), pain_extract.extract_pains_task(), goal_extract.extract_goals_task()]
        )
        return synthesize_persona_task

synthesizer_maker = SynthesizerAgent()
