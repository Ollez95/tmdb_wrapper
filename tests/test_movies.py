#!/usr/bin/env python
import pytest
import unittest

from keys import API_KEY, LANGUAGE, REGION, ERROR_MOVIE
from tests.keys import PASSWORD, USERNAME
from tmdb_wrapper.tmdb.authentication import Authentication

from tmdb_wrapper.tmdb.base import TMDb
from tmdb_wrapper.tmdb.movies import Movies


class TestTMDb_Movies(unittest.TestCase):
    """Tests for `tmdb_api` package."""

    def setUp(self):
        """Set up API keys"""
        tmdb = TMDb()
        tmdb.api_key = API_KEY
        tmdb.language = LANGUAGE
        tmdb.region = REGION
        
        self.authentication = Authentication()
        self.authentication.username = USERNAME
        self.authentication.password = PASSWORD

        self.authentication.initialize_session_id(type_session="user_session")


    def test_movie_get_details(self):
        """
        test movies get_details_movie
        """
        
        movies = Movies()

        response = movies.get_details_movie(
            movie_id=5
        )
        assert response != ERROR_MOVIE
        
    def test_movie_account_states(self):
        """
        test movies get_details_movie
        """
        
        movies = Movies()

        response = movies.get_account_states(
            movie_id=5
        )
        assert response != ERROR_MOVIE


    def test_movie_alternative_titles(self):
        """
        test movies get_alternative_titles
        """
        movies = Movies()
        response = movies.get_alternative_titles(
            movie_id=5
        )
        print(movies.api_key)
        assert response != ERROR_MOVIE

    def test_movie_get_changes(self):
        """
        test movies get_changes
        """
        movies = Movies()
        response = movies.get_changes(
            movie_id = 111,
            start_date="2016-08-29",
            end_date="2016-09-10"
        )
        assert str(response) != str(ERROR_MOVIE)

    def test_movie_get_credits(self):
        """
        test movies get_credits
        """
        movies = Movies()
        response = movies.get_credits(
            movie_id = 111
        )

        assert str(response) != str(ERROR_MOVIE)


    def test_movie_get_external_ids(self):
        """
        test movies get_external_ids
        """
        movies = Movies()
        response = movies.get_external_ids(
            movie_id = 111
        )

        assert str(response) != str(ERROR_MOVIE)

    def test_movie_get_keywords(self):
        """
        test movies get_keywords
        """
        movies = Movies()
        response = movies.get_keywords(
            movie_id = 111
        )

        assert str(response) != str(ERROR_MOVIE)


    def test_movie_get_lists(self):
        """
        test movies get_lists
        """
        movies = Movies()
        response = movies.get_lists(
            movie_id = 2
        )

        assert str(response) != str(ERROR_MOVIE)


    def test_movie_get_recommendations(self):
        """
        test movies get_recommendations
        """
        movies = Movies()
        response = movies.get_recommendations(
            movie_id = 3
        )

        assert str(response) != str(ERROR_MOVIE)

    def test_movie_get_release_dates(self):
        """
        test movies get_release_dates
        """
        movies = Movies()
        response = movies.get_release_dates(
            movie_id = 3
        )

        assert str(response) != str(ERROR_MOVIE)

    def test_movie_get_reviews(self):
        """
        test movies get_reviews
        """
        movies = Movies()
        response = movies.get_reviews(
            movie_id = 200
        )

        assert str(response) != str(ERROR_MOVIE)

    def test_movie_get_similar(self):
        """
        test movies get_similar_movies
        """
        movies = Movies()
        response = movies.get_similar_movies(
            movie_id = 200,
            page=2
        )

        assert str(response) != str(ERROR_MOVIE)

    def test_movie_translations(self):
        """
        test movies get_translations
        """
        movies = Movies()
        response = movies.get_translations(
            movie_id = 200,
        )

        assert response != ERROR_MOVIE

    def test_movie_get_video(self):
        """
        test movies get_videos
        """
        movies = Movies()
        response = movies.get_videos(
            movie_id = 200,
            include_video_language = "pt"
        )

        assert str(response) != str(ERROR_MOVIE)
        
    def test_movie_post_rate_movie(self):
        """
        test movies get_videos
        """
        movies = Movies()
        response = movies.post_rate_movie(
            movie_id = 200,
            value = 5
        )

        assert str(response) != str(ERROR_MOVIE)
        
    def test_movie_delete_video(self):
        """
        test movies get_videos
        """
        movies = Movies()
        response = movies.delete_video(
            movie_id = 200
        )

        assert str(response) != str(ERROR_MOVIE)

    def test_movie_latest(self):
        """
        test movies get_latest
        """
        movies = Movies()
        response = movies.get_latest(
        )

        assert str(response) != str(ERROR_MOVIE)

    def test_movie_now_playing(self):
        """
        test movies get_now_playing
        """
        movies = Movies()
        response = movies.get_now_playing(
        )

        assert str(response) != str(ERROR_MOVIE)


    def test_movie_popular(self):
        """
        test movies get_popular
        """
        movies = Movies()
        response = movies.get_popular(
        )

        assert str(response) != str(ERROR_MOVIE)

    def test_movie_top_rated(self):
        """
        test movies get_top_rated
        """
        movies = Movies()
        response = movies.get_top_rated(
        )

        assert str(response) != str(ERROR_MOVIE)


    def test_movie_upcoming(self):
        """
        test movies get_upcoming
        """
        movies = Movies()
        response = movies.get_upcoming(
        )

        assert str(response) != str(ERROR_MOVIE)

if __name__ == "__main__":
    unittest.main()