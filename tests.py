import os

class Base:
    TMDB_URL = "https://api.themoviedb.org"
    TMDB_VERSION = "3"
    TMDB_KEY = "TMDB_KEY"
    TMDB_LANGUAGE = "TMDB_LANGUAGE"
    TMDB_REGION = "TMDB_REGION"

    def __init__(
        self,
        *,
        language: str = None,
        region: str = None,
    ):
        self._language = language if language is not None else os.environ.get(self.TMDB_LANGUAGE, "en-US")
        self._region = region if region is not None else os.environ.get(self.TMDB_REGION, "US")

    @property
    def host(self) -> str:
        return self.TMDB_URL

    @property
    def version(self) -> str:
        return self.TMDB_VERSION

    @property
    def key(self) -> str:
        return os.environ.get(self.TMDB_KEY)

    @key.setter
    def key(self, key: str) -> None:
        os.environ[self.TMDB_KEY] = key

    @property
    def language(self) -> str:
        return self._language

    @language.setter
    def language(self, language: str) -> None:
        self._language = language

    @property
    def region(self) -> str:
        return self._region

    @region.setter
    def region(self, region: str) -> None:
        self._region = region

    @property
    def default_params(self) -> dict:
        return {
            "api_key": self.key,
            "language": self.language,
            "region": self.region,
            "watch_region": self.region,
        }

class Movie(Base):
    pass


base = Base()

base.key = "asffas"

movie = Movie()

print(os.environ)