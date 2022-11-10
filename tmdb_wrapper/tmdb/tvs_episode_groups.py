from typing import Any
from tmdb_wrapper.data.tv import TvEpisodeGroup, TvSeason
from tmdb_wrapper.tmdb.base import TMDb
from tmdb_wrapper.tmdb.datatype import Datatype, ModelDatatype

from .request import GetRequest

class TvEpisodeGroups(TMDb):

    def get_details(
        self,
        id: int = None,
        datatype : Datatype = ModelDatatype()) -> Any:
        '''
        Get the details of a TV episode group. Groups support 7 different types which are enumerated as the following:

        Original air date
        Absolute
        DVD
        Digital
        Story arc
        Production
        TV

        See more: https://developers.themoviedb.org/3/tv-episode-groups/get-tv-episode-group-details
        '''

        parse_data = self.request_data(
            request_operation = GetRequest(),
            path = f"/tv/episode_group/{id}")

        return datatype.to_datatype(parse_data = parse_data, model_data = TvEpisodeGroup)