from ninja import Schema


class Item(Schema):
    name: str
    description: str = ""
    price: float
    quantity: int


@api.post("/items")
def create(request, item: Item):
    return item
