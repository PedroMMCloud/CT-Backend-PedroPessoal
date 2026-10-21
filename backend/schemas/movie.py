from typing import List, Optional

from pydantic import BaseModel

class MovieSchema(BaseModel):
    id: int
    title: str
    summary: Optional[str] = None
    image: Optional[str] = None
    rating: Optional[float] = None
    genres: List[str] = []