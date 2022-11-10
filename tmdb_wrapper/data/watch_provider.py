from dataclasses import dataclass
from typing import Optional


@dataclass
class WatchProviderRegion:
    iso_3166_1: Optional[str]
    english_name: Optional[str]
    native_name: Optional[str]


@dataclass
class WatchMovieProvider:
    display_priority: Optional[int]
    logo_path: Optional[str]
    provider_name: Optional[str]
    provider_id: Optional[str]

@dataclass
class WatchMovieProviders:
    results: Optional[list[WatchMovieProvider]]

@dataclass
class WatcTvProviders:
    results: Optional[list[WatchMovieProvider]]