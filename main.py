import os
from crewai import Crew
from schema import RedditExtractionOutput
from agents.data_extractor import data_extract  
from agents.content_analyzer import content_analyze
from agents.interest_agent import interest_extract
from agents.personality_agent import personality_extract
from agents.pain_agent import pain_extract
from agents.goal_agent import goal_extract
from agents.synthesizer import synthesizer_maker


agents = [data_extract.extract_data_agent(),content_analyze.analyze_content_agent(), 
            interest_extract.extract_interest_agent(), personality_extract.extract_personality_agent(), 
            pain_extract.extract_pain_agent(), goal_extract.extract_goal_agent(), synthesizer_maker.extract_synthesizer_agent()
        ]
tasks = [data_extract.extract_data_task(),content_analyze.analyze_content_task(),
            interest_extract.extract_interests_task(), personality_extract.extract_personality_task(), 
            pain_extract.extract_pains_task(), goal_extract.extract_goals_task(), synthesizer_maker.synthesize_persona_task()
        ]
# Create Crew
crew = Crew(
    agents=agents,
    tasks=tasks,
    verbose=True
)

def build_user_persona(reddit_url: str) -> RedditExtractionOutput:
    """Build and save a user persona using RedditExtractionTool and CrewAI."""
    # Extract username from URL
    if reddit_url[-1] == "/":
        username = reddit_url.split("/")[-2]
    else:
        username = reddit_url.split("/")[-1]
        
    result = crew.kickoff(inputs={"username": username})
    return result.raw

if __name__ == "__main__":
    reddit_url = input("Enter the Reddit URL: ")
    response = build_user_persona(reddit_url)
    # Save persona to text file
    output_dir = "personas"
    os.makedirs(output_dir, exist_ok=True)
    if reddit_url[-1] == "/":
        username = reddit_url.split("/")[-2]
    else:
        username = reddit_url.split("/")[-1]
    output_path = os.path.join(output_dir, f"{username}_persona.txt")
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(response)

    print(f"User persona saved to {output_path}")