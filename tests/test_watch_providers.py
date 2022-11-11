import unittest
from tmdb_wrapper.tmdb.base import TMDb
from keys import API_KEY, ERROR_MOVIE, LANGUAGE, REGION, USERNAME, PASSWORD
from tmdb_wrapper.tmdb.watch_providers import WatchProviders

class TestTMDb_WatchProviders(unittest.TestCase):

    '''
    Watch Providers Class
    '''

    def setUp(self):
        """Set up API keys"""
        self.tmdb = TMDb()
        self.tmdb.api_key = API_KEY
        self.tmdb.language = LANGUAGE
        self.tmdb.region = REGION

    def test_get_available_regions(self):
        """
        test watch providers get_available_regions
        """

        watch_providers = WatchProviders()

        response = watch_providers.get_available_regions()

        print(response)

        assert response != ERROR_MOVIE

    def test_get_movie_providers(self):
        """
        test watch providers get_movie_providers
        """

        watch_providers = WatchProviders()

        response = watch_providers.get_movie_providers()

        print(response)

        assert response != ERROR_MOVIE

    def test_get_tv_providers(self):
        """
        test watch providers get_tv_providers
        """

        watch_providers = WatchProviders()

        response = watch_providers.get_tv_providers()

        print(response)

        assert response != ERROR_MOVIE