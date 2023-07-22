from pandas import DataFrame

from .type import Movie
from .fetch_poster import fetch_poster


async def recommend(dataset: DataFrame, similarity, movie: str | None):
    idx = dataset[dataset["title"] == movie].index[0]
    dst = similarity[idx]
    lst = sorted(list(enumerate(dst)), reverse=True, key=lambda x: x[1])[1:6]

    offset = lambda i: dataset.iloc[i[0]]
    return [ Movie(title=offset(i).title, poster=await fetch_poster(offset(i).movie_id)) for i in lst ]
