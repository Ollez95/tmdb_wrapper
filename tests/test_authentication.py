import unittest
from tmdb_api.tmdb.authentication import Authentication

from tmdb_api.tmdb.configurations import Configurations
from tmdb_api.tmdb.base import TMDb
from tmdb_api.tmdb.datatype import PrettifyDatatype
from keys import API_KEY, ERROR_MOVIE, LANGUAGE, REGION, USERNAME, PASSWORD

class TestTMDb_Authentication(unittest.TestCase):

    def setUp(self):
        """Set up API keys"""
        self.tmdb = TMDb()
        self.tmdb.api_key = API_KEY
        self.tmdb.language = LANGUAGE
        self.tmdb.region = REGION

    def test_guest_authentication(self):
        '''
        test_authentication
        '''

        authentication = Authentication()
        authentication.username = USERNAME
        authentication.password = PASSWORD

        authentication.initialize_session_id(
            type_session="guest_session"
        )

        print(authentication.expires_at)
        print(authentication.session_id)

    def test_user_authentication(self):
        '''
        test_authentication
        '''

        authentication = Authentication()
        authentication.username = USERNAME
        authentication.password = PASSWORD

        authentication.initialize_session_id(type_session="user_session"
        )

        print(authentication.expires_at)
        print(authentication.session_id)
        print(authentication.request_token)

    def test_user_delete_session(self):

        authentication = Authentication()
        authentication.username = USERNAME
        authentication.password = PASSWORD

        authentication.initialize_session_id(type_session="user_session")

        print(authentication.session_id)

        authentication.delete_session()