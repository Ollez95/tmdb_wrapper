import unittest
from tmdb_wrapper.tmdb.authentication import Authentication
from tmdb_wrapper.tmdb.base import TMDb
from keys import API_KEY, ERROR_MOVIE, LANGUAGE, REGION, USERNAME, PASSWORD
from tmdb_wrapper.tmdb.tvs_seasons import TvSeasons

class TestTMDb_TvSeason(unittest.TestCase):

    def setUp(self):
        """Set up API keys"""
        self.tmdb = TMDb()
        self.tmdb.api_key = API_KEY
        self.tmdb.language = LANGUAGE
        self.tmdb.region = REGION

        self.authentication = Authentication()
        self.authentication.username = USERNAME
        self.authentication.password = PASSWORD

        self.authentication.initialize_session_id(type_session="user_session")

    def test_get_details(self):
        """Test something."""
    
        tvs_season = TvSeasons()

        response = tvs_season.get_details(
            tv_id=3624,
            season_number=1
        )

        print(response)

        assert response != ERROR_MOVIE

    def test_get_account_settings(self):
        """Test something."""
    
        tvs_season = TvSeasons()

        response = tvs_season.get_account_settings(
            tv_id=3624,
            season_number=1
        )

        print(response)

        assert response != ERROR_MOVIE

    def test_get_aggregate_credits(self):
        """Test something."""
    
        tvs_season = TvSeasons()

        response = tvs_season.get_aggregate_credits(
            tv_id=3624,
            season_number=1
        )

        print(response)

        assert response != ERROR_MOVIE

    def test_get_changes(self):
        """Test something."""

        tvs_season = TvSeasons()

        response = tvs_season.get_changes(
            tv_id=3624,
            season_number=1,
            start_date="2016-04-20",
            end_date="2022-04-20"
        )

        print(response)

        assert response != ERROR_MOVIE

    def test_get_credits(self):
        """Test something."""
     
        tvs_season = TvSeasons()

        response = tvs_season.get_credits(
            tv_id=3624,
            season_number=1
        )

        print(response)

        assert response != ERROR_MOVIE

    def test_get_external_ids(self):
        """Test something."""
     
        tvs_season = TvSeasons()

        response = tvs_season.get_external_ids(
            tv_id=3624,
            season_number=1
        )

        print(response)

        assert response != ERROR_MOVIE

    def test_get_images(self):
        """Test something."""
    
        tvs_season = TvSeasons()

        response = tvs_season.get_images(
            tv_id=3624,
            season_number=1
        )

        print(response)

        assert response != ERROR_MOVIE

    def test_get_translations(self):
        """Test something."""
 
        tvs_season = TvSeasons()

        response = tvs_season.get_translations(
            tv_id=3624,
            season_number=1
        )

        print(response)

        assert response != ERROR_MOVIE

    def test_get_videos(self):
        """Test something."""

        tvs_season = TvSeasons()

        response = tvs_season.get_videos(
            tv_id=3624,
            season_number=1
        )

        print(response)

        assert response != ERROR_MOVIE
