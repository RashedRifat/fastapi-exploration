from fastapi import Depends
from typing import Union

class Increment:
    def __init__(self, inc: Union[int, None] = None) -> None:
        self.inc = inc if inc is not None else 0 

class QueryParams:
    def __init__(self, stop : int, start : int = 0, inc : Increment = Depends()) -> None:
        self.stop = stop
        self.start = start 
        self.inc = inc.inc 