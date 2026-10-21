from typing import List
import httpx
from fastapi import APIRouter, HTTPException, Query

from .movie import MovieSchema
from services.tvmaze_service import search_movies_in_tvmaze

router = APIRouter(prefix="/api/movies", tags=["Filmes"])

@router.get("/search", response_model=List[MovieSchema])
async def search_movies(q: str = Query(...)) -> List[MovieSchema]:
    try:
        return await search_movies_in_tvmaze(q)
    except httpx.HTTPError:
        raise HTTPException(
            status_code=502,
            detail="Erro ao consultar a API do TVMaze.",
        )