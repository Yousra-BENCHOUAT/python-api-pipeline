from fastapi import FastAPI

app = FastAPI(title="DevSecOps API", version="1.0.0")

@app.get("/")
def home():
    return {"message": "API is running", "status": "healthy"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/items")
def get_items():
    items = [
        {"id": 1, "name": "item one", "price": 10.5},
        {"id": 2, "name": "item two", "price": 20.0},
        {"id": 3, "name": "item three", "price": 15.75},
    ]
    return {"items": items}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    items = {
        1: {"id": 1, "name": "item one", "price": 10.5},
        2: {"id": 2, "name": "item two", "price": 20.0},
        3: {"id": 3, "name": "item three", "price": 15.75},
    }
    if item_id not in items:
        return {"error": "item not found"}
    return items[item_id]