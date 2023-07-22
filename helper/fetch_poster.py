from typing import Union
from aiohttp import ClientSession
from numpy import int64

from config import API


async def fetch_poster(id_: Union[int, int64]):
    async with ClientSession() as session:
        async with session.get(f"https://api.themoviedb.org/3/movie/{id_}?api_key={API}&language=en-US") as response:
            movie = await response.json()
            poster_path = movie["poster_path"]
            url = f"https://image.tmdb.org/t/p/w500/{poster_path}"
            return url
