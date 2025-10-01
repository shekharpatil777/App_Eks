from typing import Annotated
from fastapi import FastAPI, Path, Query

app = FastAPI()


async def read_items(
    # Path parameter with a title, description, and minimum value of 1.
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=1)],
    
    # Query parameter that is required, has a max length of 50, and a regex.
    q: Annotated[
        str,
        Query(
            title="Query string",
            description="A query string to search for items.",
            min_length=3,
            max_length=50,
            regex="^fixedquery$"
        )
    ],
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results