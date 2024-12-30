from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas

router = APIRouter(prefix="/logs", tags=["Logs"])

@router.get("/", response_model=list[schemas.Log])
def get_all_logs(db: Session = Depends(get_db)):
    return db.query(models.Log).all()

@router.post("/", response_model=schemas.Log)
def create_log(log_data: schemas.LogCreate, db: Session = Depends(get_db)):
    new_log = models.Log(log_type=log_data.log_type, message=log_data.message)
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    return new_log

@router.get("/{log_id}", response_model=schemas.Log)
def get_log(log_id: int, db: Session = Depends(get_db)):
    log_record = db.query(models.Log).filter(models.Log.id == log_id).first()
    if not log_record:
        raise HTTPException(status_code=404, detail="Log not found")
    return log_record

@router.put("/{log_id}", response_model=schemas.Log)
def update_log(log_id: int, log_data: schemas.LogCreate, db: Session = Depends(get_db)):
    log_record = db.query(models.Log).filter(models.Log.id == log_id).first()
    if not log_record:
        raise HTTPException(status_code=404, detail="Log not found")
    log_record.log_type = log_data.log_type
    log_record.message = log_data.message
    db.commit()
    db.refresh(log_record)
    return log_record

@router.delete("/{log_id}")
def delete_log(log_id: int, db: Session = Depends(get_db)):
    log_record = db.query(models.Log).filter(models.Log.id == log_id).first()
    if not log_record:
        raise HTTPException(status_code=404, detail="Log not found")
    db.delete(log_record)
    db.commit()
    return {"detail": f"Log with id {log_id} deleted"}