from pydantic import BaseModel
from typing import Optional

class QueryParameter(BaseModel):
    chatbot_query: Optional[str] = None

