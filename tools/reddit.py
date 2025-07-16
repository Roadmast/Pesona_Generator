from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from config import settings
from typing import Type
import praw
import json

# Define the input schema for the tool
class RedditExtractionInput(BaseModel):
    """Input schema for RedditExtractionTool."""
    username: str = Field(..., description="The username of the Reddit user to extract data from.")

class RedditExtractionTool(BaseTool):
    name: str = "Reddit Extraction Tool"
    description: str = "Extracts comments and posts from a given Reddit username."
    args_schema: Type[BaseModel] = RedditExtractionInput

    def _run(self, username: str) -> str:
        """Extracts comments and posts from a Reddit user."""

        try:
            reddit = praw.Reddit(
                client_id=settings.Client_ID,
                client_secret=settings.Client_Secret,
                user_agent=settings.User_Agent,
                check_for_async=False
            )
        except Exception as e:
            return f"Error connecting to Reddit API: {e}"

        try:
            # Get the user object
            user = reddit.redditor(username)

            extracted_data = []

            # Extract comments (limit to 10 for demonstration)
            for comment in user.comments.new(limit=50):
                extracted_data.append({
                    "source": "comment",
                    "title": comment.submission.title,
                    "comments": comment.body
                })

            # Extract posts (submissions) (limit to 10 for demonstration)
            for submission in user.submissions.new(limit=50):
                extracted_data.append({
                    "source": "post",
                    "title": submission.title,
                    "selftext": submission.selftext
                })

            # Return data as a JSON string
            return json.dumps(extracted_data, indent=4)

        except Exception as e:
            return f"Error extracting data for user {username}: {e}"