from pydantic import BaseModel, Field
from typing import Optional, Dict

class QueryParameter(BaseModel):
    # page: int = Field(1, ge=1)
    # limit: int = Field(20, ge=1, le=100)
    search: Optional[str] = None
    sort_by: str = "id"
    order: str = "asc"
    product_category: Optional[str] = None
    product_attribute: Dict[str, str] = Field(default_factory=dict)
    product_brand: Optional[str] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None