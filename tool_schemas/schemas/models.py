from typing import List
from pydantic import BaseModel


class Model(BaseModel):
    item: List[str]
