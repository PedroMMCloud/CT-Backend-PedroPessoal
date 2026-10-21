import html
import re
from typing import List, Optional
import httpx

from movie import MovieSchema

TVMAZE_SEARCH_URL = "https://api.tvmaze.com/search/shows"

_HTML_TAG_RE = re.compile(r"<[^>]+>")


def clean_html(text: Optional[str]) -> Optional[str]:
    if not text:
        return None
    cleaned = _HTML_TAG_RE.sub("", text)
    cleaned = html.unescape(cleaned).strip()
    return cleaned or None


async def search_movies_in_tvmaze(query: str) -> List[MovieSchema]:
    if not query or not query.strip():
        return []

    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(TVMAZE_SEARCH_URL, params={"q": query.strip()})
        response.raise_for_status()
        results = response.json()

    movies: List[MovieSchema] = []
    for item in results:
        show = item.get("show", {})
        image = show.get("image") or {}
        rating = show.get("rating") or {}

        movies.append(
            MovieSchema(
                id=show["id"],
                title=show["name"],
                summary=clean_html(show.get("summary")),
                image=image.get("medium"),
                rating=rating.get("average"),
                genres=show.get("genres") or [],
            ))

    return movies