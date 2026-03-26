from datetime import date
from pydantic import BaseModel


class BorrowingBase(BaseModel):
    book_id: int
    borrower_name: str
    borrowed_at: date
    returned_at: date | None = None


class BorrowingCreate(BorrowingBase):
    pass


class BorrowingRead(BorrowingBase):
    id: int

    class Config:
        from_attributes = True
