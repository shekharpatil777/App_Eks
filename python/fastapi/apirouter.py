from fastapi import APIRouter

# Create a new router instance
router = APIRouter(
    prefix="/items", # All paths in this router will be prefixed with /items
    tags=["items"],   # Groups endpoints in the OpenAPI docs
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_items():
    return [{"name": "Item Foo"}, {"name": "Item Bar"}]

@router.get("/{item_id}")
async def read_item(item_id: str):
    return {"name": "Fake Specific Item", "item_id": item_id}