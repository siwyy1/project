from datetime import date
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.book import Book
from app.models.borrowing import Borrowing
from app.schemas.borrowing import BorrowingCreate, BorrowingRead

router = APIRouter(prefix="/borrowings", tags=["borrowings"])


@router.get("/", response_model=list[BorrowingRead])
def list_borrowings(db: Session = Depends(get_db)):
    return db.query(Borrowing).all()


@router.get("/{borrowing_id}", response_model=BorrowingRead)
def get_borrowing(borrowing_id: int, db: Session = Depends(get_db)):
    borrowing = db.query(Borrowing).filter(Borrowing.id == borrowing_id).first()
    if not borrowing:
        raise HTTPException(status_code=404, detail="Borrowing not found")
    return borrowing


@router.post("/", response_model=BorrowingRead, status_code=201)
def create_borrowing(borrowing: BorrowingCreate, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == borrowing.book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db_borrowing = Borrowing(**borrowing.model_dump())
    db.add(db_borrowing)
    db.commit()
    db.refresh(db_borrowing)
    return db_borrowing


@router.patch("/{borrowing_id}/return", response_model=BorrowingRead)
def return_book(borrowing_id: int, db: Session = Depends(get_db)):
    borrowing = db.query(Borrowing).filter(Borrowing.id == borrowing_id).first()
    if not borrowing:
        raise HTTPException(status_code=404, detail="Borrowing not found")
    if borrowing.returned_at is not None:
        raise HTTPException(status_code=409, detail="Book already returned")
    borrowing.returned_at = date.today()
    db.commit()
    db.refresh(borrowing)
    return borrowing

