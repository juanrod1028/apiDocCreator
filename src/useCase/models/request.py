from typing import Optional, Dict
from pydantic import BaseModel, Field


class Request(BaseModel):
    method: str
    body: Optional[Dict] = Field(default={})
    queryString: Optional[str] = Field(
        None, description="Query string para GET")
    path: Optional[str] = Field(None, description="Path para GET")
