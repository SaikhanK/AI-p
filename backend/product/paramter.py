from pydantic import BaseModel

class QueryParameter(BaseModel):
    name: str