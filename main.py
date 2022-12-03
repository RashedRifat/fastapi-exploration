from typing import Union
from fastapi import FastAPI, Depends
from dependencies.query import QueryParams

app = FastAPI()

@app.get("/")
def hello():
    """Says hello!

    Returns:
        json: {"msg" : "Hello World!"}
    """
    return {"msg" : "Hello World!"}

@app.get("/list/{stop}")
def list(stop: int, start: int = 0, inc: int = 1):
    """Generates a list of integers.

    Args:
        stop (int): the end of the list
        start (int, optional): the start of the list. Defaults to 0.
        inc (int, optional): the value to increment by. Defaults to 1.

    Returns:
        array: an array of integers from start to stop, incremented by inc
    """
    return [*range(start, stop, inc)]

@app.get('/dependency/{stop}')
def dependency(cq: QueryParams = Depends()):
    return {"queries" : cq} 