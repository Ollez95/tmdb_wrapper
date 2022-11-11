from typing import Any
from tmdb_wrapper.data.external_id import ExternalIDs
from tmdb_wrapper.data.image import Images
from tmdb_wrapper.data.tv import TvChanges, TvCredits, TvEpisodeSeason, TvResponse, TvSeasonEpisodeState, TvTranslations, TvVideos
from tmdb_wrapper.tmdb.authentication import Authentication
from tmdb_wrapper.tmdb.base import TMDb
from tmdb_wrapper.tmdb.datatype import Datatype, ModelDatatype
from tmdb_wrapper.tmdb.excep import TMDbException
from tmdb_wrapper.utils.helpers import init_session_type
from tmdb_wrapper.utils.constants import url_header_encoded

from .request import DeleteRequest, GetRequest, PostRequest

class TvEpisodes(Authentication):

    def __init__(self):
        super().__init__()
        if self.session_id is None:
            raise TMDbException("You need to initialize a guest session or user session'")

    def get_details(
        self,
        tv_id: int,
        datatype : Datatype = ModelDatatype(),
        season_number: int = None,
        episode_number: int = None,
        append_to_response: str = None) -> Any:
        '''
        Get the TV episode details by id.

        Supports append_to_response. Read more about this.

        See more: https://developers.themoviedb.org/3/tv-episodes/get-tv-episode-details
        '''

        parse_data = self.request_data(
            request_operation = GetRequest(),
            path = f"/tv/{tv_id}/season/{season_number}/episode/{episode_number}",
            append_to_response = append_to_response)

        return datatype.to_datatype(parse_data = parse_data, model_data = TvEpisodeSeason)

    def get_account_settings(
        self,
        tv_id: int,
        datatype : Datatype = ModelDatatype(),
        season_number: int = None,
        episode_number: int = None) -> Any:
        '''
        Get your rating for a episode.

        See more: https://developers.themoviedb.org/3/tv/get-tv-season-account-states
        '''

        def aux_init_session_type(**kwargs):
            return init_session_type(
                        request_data = self.request_data,
                        request_operation= GetRequest(),
                        path = f"/tv/{tv_id}/season/{season_number}/episode/{episode_number}/account_states",
                        **kwargs
                        )

        if self.type_session == "guest_session":
            parse_data = aux_init_session_type(guest_session_id = self.session_id)

        else:
            parse_data = aux_init_session_type(session_id = self.session_id)

        return datatype.to_datatype(parse_data = parse_data, model_data = TvSeasonEpisodeState)


    def get_changes(
        self,
        episode_id: int,
        datatype : Datatype = ModelDatatype(),
        start_date: str = None,
        end_date: str = None,
        page: int = 1) -> Any:
        '''
        Get the changes for a TV episode. By default only the last 24 hours are returned.

        You can query up to 14 days in a single query by using the start_date and end_date
        query parameters.

        See more: https://developers.themoviedb.org/3/tv/get-tv-season-account-states
        '''

        parse_data = self.request_data(
            request_operation = GetRequest(),
            path = f"/tv/episode/{episode_id}/changes",
            start_date = start_date,
            end_date = end_date,
            page = page)

        return datatype.to_datatype(parse_data = parse_data, model_data = TvChanges)

    def get_credits(
        self,
        tv_id: int,
        datatype : Datatype = ModelDatatype(),
        season_number: int = None,
        episode_number: int = None) -> Any:
        '''
        Get the credits for TV season.

        See more: https://developers.themoviedb.org/3/tv-seasons/get-tv-season-credits
        '''

        parse_data = self.request_data(
                request_operation = GetRequest(),
                path = f"/tv/{tv_id}/season/{season_number}/episode/{episode_number}/credits")


        return datatype.to_datatype(parse_data = parse_data, model_data = TvCredits)

    def get_external_ids(
        self,
        tv_id: int,
        datatype : Datatype = ModelDatatype(),
        season_number: int = None,
        episode_number: int = None) -> Any:
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
                path = f"/tv/{tv_id}/season/{season_number}/episode/{episode_number}/external_ids")


        return datatype.to_datatype(parse_data = parse_data, model_data = ExternalIDs)

    def get_images(
        self,
        tv_id: int,
        datatype : Datatype = ModelDatatype(),
        season_number: int = None,
        episode_number: int = None) -> Any:
        '''
        Get the images that belong to a TV episode.

        Querying images with a language parameter will filter the results.
        If you want to include a fallback language (especially useful for backdrops)
        you can use the include_image_language parameter. This should be a comma
        seperated value like so: include_image_language=en,null.


        See more: https://developers.themoviedb.org/3/tv-seasons/get-tv-season-images
        '''

        parse_data = self.request_data(
                request_operation = GetRequest(),
                path = f"/tv/{tv_id}/season/{season_number}/episode/{episode_number}/images")


        return datatype.to_datatype(parse_data = parse_data, model_data = Images)

    def get_translations(
        self,
        tv_id: int,
        datatype : Datatype = ModelDatatype(),
        season_number: int = None,
        episode_number: int = None) -> Any:
        '''
        Get the translation data for an episode.

        See more: https://developers.themoviedb.org/3/tv-episodes/get-tv-episode-translations
        '''

        parse_data = self.request_data(
                request_operation = GetRequest(),
                path = f"/tv/{tv_id}/season/{season_number}/episode/{episode_number}/translations")


        return datatype.to_datatype(parse_data = parse_data, model_data = TvTranslations)

    def post_rate_episode(
        self,
        tv_id: int,
        datatype : Datatype = ModelDatatype(),
        season_number: int = None,
        episode_number: int = None,
        value: float = 0.5) -> Any:
        '''
        A valid session or guest session ID is required. You can read more about how this works .

        See more: https://developers.themoviedb.org/3/tv/rate-tv-show
        '''

        def aux_init_session_type(**kwargs):
            return init_session_type(
                        request_data = self.request_data,
                        request_operation= PostRequest(),
                        path = f"/tv/{tv_id}/season/{season_number}/episode/{episode_number}/rating",
                        data = {
                        "value":value
                        },
                        headers=url_header_encoded,
                        **kwargs
                        )

        if self.type_session == "guest_session":
            parse_data = aux_init_session_type(guest_session_id = self.session_id)

        else:
            parse_data = aux_init_session_type(session_id = self.session_id)


        return datatype.to_datatype(
            parse_data = parse_data,
            model_data = TvResponse)

    def delete_video(
        self,
        tv_id: int,
        datatype : Datatype = ModelDatatype(),
        season_number: int = None,
        episode_number: int = None,) -> Any:
        '''
        Remove your rating for a TV episode.

        A valid session or guest session ID is required.
        You can read more about how this works .   

        See more: https://developers.themoviedb.org/3/tv-episodes/delete-tv-episode-rating
        '''

        def aux_init_session_type(**kwargs):
            return init_session_type(
                        request_data = self.request_data,
                        request_operation= DeleteRequest(),
                        path = f"/tv/{tv_id}/season/{season_number}/episode/{episode_number}/rating",
                        headers=url_header_encoded,
                        **kwargs
                        )

        if self.type_session == "guest_session":
            parse_data = aux_init_session_type(guest_session_id = self.session_id)

        else:
            parse_data = aux_init_session_type(session_id = self.session_id)


        return datatype.to_datatype(
            parse_data = parse_data,
            model_data = TvResponse)

    def get_videos(
        self,
        tv_id: int,
        datatype : Datatype = ModelDatatype(),
        season_number: int = None,
        episode_number: int = None) -> Any:
        '''
        Get the videos that have been added to a TV season.

        See more: https://developers.themoviedb.org/3/tv-seasons/get-tv-season-videos
        '''

        parse_data = self.request_data(
                request_operation = GetRequest(),
                path = f"/tv/{tv_id}/season/{season_number}/episode/{episode_number}/videos")


        return datatype.to_datatype(parse_data = parse_data, model_data = TvVideos)