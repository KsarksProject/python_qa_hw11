from dataclasses import dataclass
from typing import List


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    birth_day: str
    birth_month: str
    birth_year: str
    subjects: List[str]
    hobby: str
    picture: str
    address: str
    state: str
    city: str
