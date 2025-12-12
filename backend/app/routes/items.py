from fastapi import APIRouter, Depends, HTTPException
from app.database import SessionLocal
from app.models import Item

items_router = APIRouter()

@items_router.post("/")
def create_item(title: str, description: str):
    session = SessionLocal()
    new_item = Item(title=title, description=description)
    session.add(new_item)
    session.commit()
    return {"item": new_item, "id": new_item.id}

@items_router.get("/")
def get_items():
    session = SessionLocal()
    items = session.query(Item).all()
    return {"items": items, "total": len(items)}

@items_router.put("/{id}")
def update_item(id: int, title: str, description: str):
    session = SessionLocal()
    item = session.query(Item).filter_by(id=id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item.title = title
    item.description = description
    session.commit()
    return {"item": item}

@items_router.delete("/{id}")
def delete_item(id: int):
    session = SessionLocal()
    item = session.query(Item).filter_by(id=id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    session.delete(item)
    session.commit()
    return {"message": "Item deleted successfully"}