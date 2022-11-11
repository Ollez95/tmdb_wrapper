import unittest
from tmdb_wrapper.tmdb.authentication import Authentication
from tmdb_wrapper.tmdb.base import TMDb
from keys import API_KEY, ERROR_MOVIE, LANGUAGE, REGION, USERNAME, PASSWORD
from tmdb_wrapper.tmdb.tvs_episode_groups import TvEpisodeGroups

class TestTMDb_TvEpisodesGroup(unittest.TestCase):

    def setUp(self):
        """Set up API keys"""
        self.tmdb = TMDb()
        self.tmdb.api_key = API_KEY
        self.tmdb.language = LANGUAGE
        self.tmdb.region = REGION


    def test_get_details(self):
        """
        test tv_episode_groups get_details
        """
 
        tvs_episodes_group = TvEpisodeGroups()

        response = tvs_episodes_group.get_details(
            id_group="5acf93e60e0a26346d0000ce"
        )

        print(response)

        assert response != ERROR_MOVIE