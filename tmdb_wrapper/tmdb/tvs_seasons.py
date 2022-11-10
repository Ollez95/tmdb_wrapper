from typing import Any
from tmdb_wrapper.data.external_id import ExternalIDs
from tmdb_wrapper.data.image import Images
from tmdb_wrapper.data.tv import TvChanges, TvCredits, TvSeason, TvSeasonAccountStates, TvTranslations, TvVideos
from tmdb_wrapper.tmdb.authentication import Authentication
from tmdb_wrapper.tmdb.base import TMDb
from tmdb_wrapper.tmdb.datatype import Datatype, ModelDatatype
from tmdb_wrapper.utils.helpers import init_session_type

from .request import GetRequest

class TvSeasons(Authentication):

    def get_details(
        self,
        tv_id: int,
        datatype : Datatype = ModelDatatype(),
        season_number: int = None,
        append_to_response: str = None) -> Any:
        '''
        Get the TV season details by id.

        Supports append_to_response. Read more about this .

        See more: https://developers.themoviedb.org/3/tv/get-tv-season-details
        '''

        parse_data = self.request_data(
            request_operation = GetRequest(), 
            path = f"/tv/{tv_id}/season/{season_number}",
            append_to_response = append_to_response)

        return datatype.to_datatype(parse_data = parse_data, model_data = TvSeason)

    def get_account_settings(
        self,
        tv_id: int,
        datatype : Datatype = ModelDatatype(),
        season_number: int = None) -> Any:
        '''
        Returns all of the user ratings for the season's episodes.

        See more: https://developers.themoviedb.org/3/tv/get-tv-season-account-states
        '''

        def aux_init_session_type(**kwargs):
            return init_session_type(
                        request_data = self.request_data,
                        request_operation= GetRequest(),
                        path = f"/tv/{tv_id}/season/{season_number}/account_states",
                        **kwargs
                        )

        if self.type_session == "guest_session":
            parse_data = aux_init_session_type(guest_session_id = self.session_id)

        else:
            parse_data = aux_init_session_type(session_id = self.session_id)

        return datatype.to_datatype(parse_data = parse_data, model_data = TvSeasonAccountStates)

    def get_aggregate_credits(
        self,
        tv_id: int,
        datatype : Datatype = ModelDatatype(),
        season_number: int = None) -> Any:
        '''
        Get the aggregate credits for TV season.

        This call differs from the main credits call in that it does not only return the season credits,
        but rather is a view of all the cast & crew for all of the episodes belonging to a season.

        See more: https://developers.themoviedb.org/3/tv/get-tv-season-account-states
        '''

        parse_data = self.request_data(
            request_operation = GetRequest(),
            path = f"/tv/{tv_id}/season/{season_number}/aggregate_credits")

        return datatype.to_datatype(parse_data = parse_data, model_data = TvCredits)

    def get_changes(
        self,
        tv_id: int,
        datatype : Datatype = ModelDatatype(),
        season_number: int = None,
        start_date: str = None,
        end_date: str = None,
        page: int = 1) -> Any:
        '''
        Get the aggregate credits for TV season.

        This call differs from the main credits call in that it does not only return the season credits,
        but rather is a view of all the cast & crew for all of the episodes belonging to a season.

        See more: https://developers.themoviedb.org/3/tv/get-tv-season-account-states
        '''

        parse_data = self.request_data(
            request_operation = GetRequest(),
            path = f"/tv/{tv_id}/season/{season_number}/aggregate_credits",
            start_date = start_date,
            end_date = end_date,
            page = page)

        return datatype.to_datatype(parse_data = parse_data, model_data = TvChanges)

    def get_credits(
        self,
        tv_id: int,
        datatype : Datatype = ModelDatatype(),
        season_number: int = None) -> Any:
        '''
        Get the credits for TV season.

        See more: https://developers.themoviedb.org/3/tv-seasons/get-tv-season-credits
        '''

        parse_data = self.request_data(
                request_operation = GetRequest(),
                path = f"/tv/{tv_id}/season/{season_number}/credits")


        return datatype.to_datatype(parse_data = parse_data, model_data = TvCredits)

    def get_external_ids(
        self,
        tv_id: int,
        datatype : Datatype = ModelDatatype(),
        season_number: int = None) -> Any:
        '''
        Get the external ids for a TV season. We currently support the following external sources.

        Media Databases
        TVDB ID
        Freebase MID*
        Freebase ID*
        TVRage ID*
        *Defunct or no longer available as a service.

        See more: https://developers.themoviedb.org/3/tv/get-tv-season-external-ids
        '''

        parse_data = self.request_data(
                request_operation = GetRequest(),
                path = f"/tv/{tv_id}/season/{season_number}/external_ids")


        return datatype.to_datatype(parse_data = parse_data, model_data = ExternalIDs)

    def get_images(
        self,
        tv_id: int,
        datatype : Datatype = ModelDatatype(),
        season_number: int = None) -> Any:
        '''
       Get the images that belong to a TV season.

        Querying images with a language parameter will filter the results. 
        If you want to include a fallback language (especially useful for backdrops)
        you can use the include_image_language parameter. This should be a comma 
        seperated value like so: include_image_language=en,null.

        See more: https://developers.themoviedb.org/3/tv-seasons/get-tv-season-images
        '''

        parse_data = self.request_data(
                request_operation = GetRequest(),
                path = f"/tv/{tv_id}/season/{season_number}/images")


        return datatype.to_datatype(parse_data = parse_data, model_data = Images)

    def get_translations(
        self,
        tv_id: int,
        datatype : Datatype = ModelDatatype(),
        season_number: int = None) -> Any:
        '''
        Get the credits for TV season.

        See more: https://developers.themoviedb.org/3/tv/get-tv-translations
        '''

        parse_data = self.request_data(
                request_operation = GetRequest(),
                path = f"/tv/{tv_id}/season/{season_number}/translations")


        return datatype.to_datatype(parse_data = parse_data, model_data = TvTranslations)

    def get_videos(
        self,
        tv_id: int,
        datatype : Datatype = ModelDatatype(),
        season_number: int = None) -> Any:
        '''
        Get the videos that have been added to a TV season.

        See more: https://developers.themoviedb.org/3/tv-seasons/get-tv-season-videos
        '''

        parse_data = self.request_data(
                request_operation = GetRequest(),
                path = f"/tv/{tv_id}/season/{season_number}/videos")


        return datatype.to_datatype(parse_data = parse_data, model_data = TvVideos)