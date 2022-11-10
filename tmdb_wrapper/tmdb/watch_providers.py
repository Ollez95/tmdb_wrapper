from typing import Any
from tmdb_wrapper.data import watch_provider
from tmdb_wrapper.data.watch_provider import  WatchMovieProviders, WatchProviderRegion
from tmdb_wrapper.tmdb.base import TMDb
from tmdb_wrapper.tmdb.datatype import Datatype, ModelDatatype

from .request import GetRequest

class WatchProviders(TMDb):

    def get_available_regions(
        self,
        datatype : Datatype = ModelDatatype()) -> Any:
        '''
        Returns a list of all of the countries we have watch provider (OTT/streaming) data for.

        See more: https://developers.themoviedb.org/3/watch-providers/get-available-regions
        '''

        parse_data = self.request_data(
            request_operation = GetRequest(),
            path = "/watch/providers/regions")

        return datatype.to_datatype(parse_data = parse_data, model_data = WatchProviderRegion)

    def get_movie_providers(
        self,
        datatype : Datatype = ModelDatatype()) -> Any:
        '''
        Returns a list of the watch provider (OTT/streaming) data we have available for movies.
        You can specify a watch_region param if you want to further filter the list by country.

        See more: https://developers.themoviedb.org/3/watch-providers/get-movie-providers
        '''

        parse_data = self.request_data(
            request_operation = GetRequest(),
            path = "/watch/providers/movie")

        return datatype.to_datatype(parse_data = parse_data, model_data = WatchMovieProviders)

    def get_tv_providers(
        self,
        datatype : Datatype = ModelDatatype()) -> Any:
        '''
        Returns a list of the watch provider (OTT/streaming) data we have available for TV series.
        You can specify a watch_region param if you want to further filter the list by country.

        See more: https://developers.themoviedb.org/3/watch-providers/get-tv-providers
        '''

        parse_data = self.request_data(
            request_operation = GetRequest(),
            path = "/watch/providers/tv")

        return datatype.to_datatype(parse_data = parse_data, model_data = watch_provider)