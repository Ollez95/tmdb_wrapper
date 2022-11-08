from dataclasses import dataclass
from typing import Optional


@dataclass
class AuthorDetails:
    name: Optional[int]
    username: Optional[str]
    avatar_path: Optional[str]
    rating: Optional[int]