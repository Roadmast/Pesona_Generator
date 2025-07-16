from pydantic import BaseModel, Field

class RedditExtractionInput(BaseModel):
    """Input schema for RedditExtractionTool."""
    username: str = Field(..., description="The username of the Reddit user to extract data from.")

class RedditExtractionOutput(BaseModel):
    """Output schema for RedditExtractionTool."""
    data: str = Field(..., description="The extracted data from the Reddit user.")

