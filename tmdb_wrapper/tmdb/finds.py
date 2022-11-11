from typing import Any
from tmdb_wrapper.data.find import Find
from tmdb_wrapper.tmdb.datatype import Datatype, ModelDatatype
from tmdb_wrapper.tmdb.request import GetRequest
from .base import TMDb

class Finds(TMDb):
    '''
    Get a movie or TV credit details by id.
    '''
    def get_find_by_id(
        self,
        datatype : Datatype = ModelDatatype(),
        external_id: str = None,
        external_source: str = None) -> Any:

        '''
        The find method makes it easy to search for objects in our database by an external id.

        This method will search all objects (movies, TV shows and people) and return the results
        in a single response.

        The supported external sources for each object are as follows.

        Media Databases
        Movies	TV Shows	TV Seasons	TV Episodes	People
        IMDb ID	✓	✓	✗	✓	✓
        TVDB ID	✗	✓	✓	✓	✗
        Freebase MID*	✗	✓	✓	✓	✓
        Freebase ID*	✗	✓	✓	✓	✓
        TVRage ID*	✗	✓	✓	✓	✓
        Social IDs
        Movies	TV Shows	TV Seasons	TV Episodes	People
        Facebook	✓	✓	✗	✗	✓
        Instagram	✓	✓	✗	✗	✓
        Twitter	✓	✓	✗	✗	✓
        *Defunct or no longer available as a service.

        https://developers.themoviedb.org/3/find/find-by-id
        '''

        parse_data = self.request_data(
            request_operation = GetRequest(),
            path = f"/find/{external_id}",
            external_source = external_source)

        return datatype.to_datatype(parse_data = parse_data, model_data = Find)

    def get_find_by_imdb(
        self,
        imdb_id: str = None) -> Any:

        '''
        Find method to search by imdb id.
        :param imdb_id: str
        :return: Find Object
        '''
        return self.get_find_by_id(external_id = imdb_id, external_source = "imdb_id")

    def get_find_by_tvdb(
        self,
        tvdb_id: str = None) -> Any:

        '''
        Find method to search by tvdb id.
        :param tvdb_id: str
        :return: Find Object
        '''
        return self.get_find_by_id(external_id = tvdb_id, external_source = "tvdb_id")


    def get_find_by_freebase_mid(
        self,
        freebase_mid: str = None) -> Any:

        '''
        Find method to search by freebase_mid.
        :param freebase_mid: str
        :return: Find Object
        '''
        return self.get_find_by_id(external_id = freebase_mid, external_source = "freebase_mid")

    def get_find_by_tvrage_id(
        self,
        tvrage_id: str = None) -> Any:

        '''
        Find method to search by tvrage_id.
        :param tvrage_id: str
        :return: Find Object
        '''
        return self.get_find_by_id(external_id = tvrage_id, external_source = "tvrage_id")

    def get_find_by_facebook_id(
        self,
        facebook_id: str = None) -> Any:

        '''
        Find method to search by facebook_id.
        :param facebook_id: str
        :return: Find Object
        '''
        return self.get_find_by_id(external_id = facebook_id, external_source = "facebook_id")

    def get_find_by_instagram_id(
        self,
        instagram_id: str = None) -> Any:

        '''
        Find method to search by instagram_id.
        :param instagram_id: str
        :return: Find Object
        '''
        return self.get_find_by_id(external_id = instagram_id, external_source = "instagram_id")

    def get_find_by_twitter_id(
        self,
        twitter_id: str = None) -> Any:

        '''
        Find method to search by twitter_id.
        :param twitter_id: str
        :return: Find Object
        '''
        return self.get_find_by_id(external_id = twitter_id, external_source = "twitter_id")
