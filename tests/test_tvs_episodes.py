import unittest
from tmdb_wrapper.tmdb.authentication import Authentication
from tmdb_wrapper.tmdb.base import TMDb
from keys import API_KEY, ERROR_MOVIE, LANGUAGE, REGION, USERNAME, PASSWORD
from tmdb_wrapper.tmdb.tvs_episodes import TvEpisodes

class TestTMDb_TvEpisodes(unittest.TestCase):

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
        """
        test tv_episode get_details
        """
    
        tvs_episodes = TvEpisodes()

        response = tvs_episodes.get_details(
            tv_id=11279,
            season_number=1,
            episode_number=1
        )

        print(response)

        assert response != ERROR_MOVIE

    def test_get_account_settings(self):
        """
        test tv_episode get_account_settings
        """
    
        tvs_episodes = TvEpisodes()

        response = tvs_episodes.get_account_settings(
            tv_id=11279,
            season_number=1,
            episode_number=1
        )

        print(response)

        assert response != ERROR_MOVIE

    def test_get_changes(self):
        """
        test tv_episode get_changes
        """
    
        tvs_episodes = TvEpisodes()

        response = tvs_episodes.get_changes(
            episode_id=123,
        )

        print(response)

        assert response != ERROR_MOVIE

    def test_get_credits(self):
        """
        test tv_episode get_credits
        """
    
        tvs_episodes = TvEpisodes()

        response = tvs_episodes.get_credits(
            tv_id=11279,
            season_number=1,
            episode_number=1
        )

        print(response)

        assert response != ERROR_MOVIE

    def test_get_external_ids(self):
        """
        test tv_episode get_external_ids
        """
    
        tvs_episodes = TvEpisodes()

        response = tvs_episodes.get_external_ids(
            tv_id=11279,
            season_number=1,
            episode_number=1
        )

        print(response)

        assert response != ERROR_MOVIE

    def test_get_images(self):
        """
        test tv_episode get_images
        """
    
        tvs_episodes = TvEpisodes()

        response = tvs_episodes.get_images(
            tv_id=11279,
            season_number=1,
            episode_number=1
        )

        print(response)

        assert response != ERROR_MOVIE

    def test_get_translations(self):
        """
        test tv_episode get_translations
        """
    
        tvs_episodes = TvEpisodes()

        response = tvs_episodes.get_translations(
            tv_id=11279,
            season_number=1,
            episode_number=1
        )

        print(response)

        assert response != ERROR_MOVIE

    def test_post_rate_episode(self):
        """
        test tv_episode post_rate_episode
        """
    
        tvs_episodes = TvEpisodes()

        response = tvs_episodes.post_rate_episode(
            tv_id=11279,
            season_number=1,
            episode_number=1,
            value=2
        )

        print(response)

        assert response != ERROR_MOVIE

    def test_delete_video(self):
        """
        test tv_episode delete_video
        """
    
        tvs_episodes = TvEpisodes()

        response = tvs_episodes.delete_video(
            tv_id=11279,
            season_number=1,
            episode_number=1
        )

        print(response)

        assert response != ERROR_MOVIE

    def test_get_videos(self):
        """
        test tv_episode get_videos
        """
    
        tvs_episodes = TvEpisodes()

        response = tvs_episodes.get_videos(
            tv_id=2,
            season_number=1,
            episode_number=1
        )

        print(response)

        assert response != ERROR_MOVIE

    
