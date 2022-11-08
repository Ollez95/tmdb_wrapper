from dataclasses import dataclass
from typing import Optional
from .media import Media

@dataclass
class Reviews:
    id: Optional[int]
    page: Optional[int]
    results: Optional[list[Media]]
    total_pages: Optional[int]
    total_results: Optional[int]