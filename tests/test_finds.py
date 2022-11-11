import unittest
from tmdb_wrapper.tmdb.authentication import Authentication
from tmdb_wrapper.tmdb.base import TMDb
from keys import API_KEY, ERROR_MOVIE, LANGUAGE, REGION, USERNAME, PASSWORD
from tmdb_wrapper.tmdb.finds import Finds

class TestTMDb_Finds(unittest.TestCase):

    '''
    Finds Class
    '''

    def setUp(self):
        """Set up API keys"""
        self.tmdb = TMDb()
        self.tmdb.api_key = API_KEY
        self.tmdb.language = LANGUAGE
        self.tmdb.region = REGION

    def test_get_find_by_id(self):
        """Test something."""

        finds = Finds()

        response = finds.get_find_by_id(
            external_id="tt0364845",
            external_source="imdb_id"
        )

        print(response)

        assert response != ERROR_MOVIE

    def test_get_find_by_imdb(self):
        """Test something."""

        finds = Finds()

        response = finds.get_find_by_imdb(
            imdb_id="tt0364845"
        )

        print(response)

        assert response != ERROR_MOVIE

    def test_get_find_by_tvdb(self):
        """Test something."""

        finds = Finds()

        response = finds.get_find_by_tvdb(
            tvdb_id="72108"
        )

        print(response)

        assert response != ERROR_MOVIE

    def test_get_find_by_freebase_mid(self):
        """Test something."""

        finds = Finds()

        response = finds.get_find_by_freebase_mid(
            freebase_mid="/m/03m8sg"
        )

        print(response)

        assert response != ERROR_MOVIE

    def test_get_find_by_tvrage_id(self):
        """Test something."""

        finds = Finds()

        response = finds.get_find_by_tvrage_id(
            tvrage_id="/en/ncis"
        )

        print(response)

        assert response != ERROR_MOVIE

    def test_get_find_by_facebook_id(self):
        """Test something."""

        finds = Finds()

        response = finds.get_find_by_facebook_id(
            facebook_id="NCIS"
        )

        print(response)

        assert response != ERROR_MOVIE

    def test_get_find_by_instagram_id(self):
        """Test something."""

        finds = Finds()

        response = finds.get_find_by_instagram_id(
            instagram_id="ncis_cbs"
        )

        print(response)

        assert response != ERROR_MOVIE

    def test_get_find_by_twitter_id(self):
        """Test something."""

        finds = Finds()

        response = finds.get_find_by_twitter_id(
            twitter_id="NCIS_CBS"
        )

        print(response)

        assert response != ERROR_MOVIE