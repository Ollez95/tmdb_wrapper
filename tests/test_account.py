import unittest
from tmdb_wrapper.tmdb.authentication import Authentication
from tmdb_wrapper.tmdb.base import TMDb
from tmdb_wrapper.tmdb.account import Account
from tmdb_wrapper.tmdb.datatype import PrettifyDatatype
from keys import API_KEY, ERROR_MOVIE, LANGUAGE, REGION, USERNAME, PASSWORD

import sys

sys.path.append("./")
print(sys.path)

class TestTMDb_Account(unittest.TestCase):

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

    def test_account(self):
        """
        test account
        """
        account = Account()
        print(account.account_id)

    def test_account_get_details(self):
        """
        test account get_details
        """
        account = Account()
        response = account.get_details()
        print(response)
        assert response != ERROR_MOVIE
    
    def test_account_get_created_lists(self):
        """
        test account get_created_lists
        """
        account = Account()
        print(account.account_id)
        response = account.get_created_lists()
        print(response)
        assert response != ERROR_MOVIE

    def test_account_get_favourite_movies(self):
        """
        test account get_favourite_movies
        """
        account = Account()
        print(account.account_id)
        response = account.get_favourite_movies()
        print(response)
        assert response != ERROR_MOVIE

    def test_account_get_favourite_tvs(self):
        """
        test account get_favourite_tvs
        """
        account = Account()
        print(account.account_id)
        response = account.get_favourite_tvs()
        print(response)
        assert response != ERROR_MOVIE

    def test_account_post_mark_as_favourite(self):
        """
        test account post_mark_as_favourite
        """
        account = Account()
        print(account.account_id)
        response = account.post_mark_as_favourite(
            media_type="movie",
            media_id=550,
            favorite="true"
        )
        print(response)
        assert response != ERROR_MOVIE

    def test_account_get_rated_movies(self):
        """
        test account get_rated_movies
        """
        account = Account()
        print(account.account_id)
        response = account.get_rated_movies()
        print(response)
        assert response != ERROR_MOVIE

    def test_account_get_tv_shows(self):
        """
        test account get_tv_shows
        """
        account = Account()
        print(account.account_id)
        response = account.get_tv_shows()
        print(response)
        assert response != ERROR_MOVIE

    def test_account_get_tv_episodes(self):
        """
        test account get_tv_episodes
        """
        account = Account()
        print(account.account_id)
        response = account.get_tv_episodes()
        print(response)
        assert response != ERROR_MOVIE

    def test_account_get_movies_watchlist(self):
        """
        test account get_movies_watchlist
        """
        account = Account()
        print(account.account_id)
        response = account.get_movies_watchlist()
        print(response)
        assert response != ERROR_MOVIE

    def test_account_get_tv_show_watchlist(self):
        """
        test account get_tv_show_watchlist
        """
        account = Account()
        print(account.account_id)
        response = account.get_tv_show_watchlist()
        print(response)
        assert response != ERROR_MOVIE

    def test_account_post_add_to_watchlist(self):
        """
        test account post_add_to_watchlist
        """
        account = Account()
        print(account.account_id)
        response = account.post_add_to_watchlist(
            media_type="movie",
            media_id=11,
            watchlist="true"
        )
        print(response)
        assert response != ERROR_MOVIE
       