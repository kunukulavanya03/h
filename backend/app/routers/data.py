from fastapi import APIRouter, Depends, HTTPException
from app.dependencies import get_db, get_current_user
from app.utils import get_jwt_token

router = APIRouter(
    prefix='/api/data',
    tags=['data'],
)

@router.get('/')
def read_data(db: Session = Depends(get_db)):
    return db.query(Data).all()

@router.get('/{item_id}')
def read_item(item_id: int, db: Session = Depends(get_db)):
    return db.query(Data).filter(Data.id == item_id).first()

@router.post('/')
def create_item(item: dict, db: Session = Depends(get_db)):
    new_item = Data(name=item['name'], description=item['description'])
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@router.put('/{item_id}')
def update_item(item_id: int, item: dict, db: Session = Depends(get_db)):
    db_item = db.query(Data).filter(Data.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail='Item not found')
    db_item.name = item['name']
    db_item.description = item['description']
    db.commit()
    return db_item

@router.delete('/{item_id}')
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Data).filter(Data.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail='Item not found')
    db.delete(db_item)
    db.commit()
    return {'message': 'Item deleted'}