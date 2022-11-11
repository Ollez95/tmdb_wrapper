from dataclasses import dataclass
from typing import Optional
from tmdb_wrapper.data.movie import Movie
from tmdb_wrapper.data.person import PersonPopular
from tmdb_wrapper.data.tv import Tv, TvEpisodeSeason, TvSeason


@dataclass
class Find:
    movie_results: Optional[list[Movie]]
    person_results: Optional[list[PersonPopular]]
    tv_results: Optional[list[Tv]]
    tv_episode_results: Optional[list[TvEpisodeSeason]]
    tv_season_results: Optional[list[TvSeason]]