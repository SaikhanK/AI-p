from pydantic import BaseModel
from typing import Optional
from typing import List

class ChatMessage(BaseModel):
    role: str
    content: str

class QueryParameter(BaseModel):
    user_input: Optional[str] = None
    history: Optional[List[ChatMessage]] = []

