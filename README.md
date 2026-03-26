# Books Borrowings

A simple REST API for managing books and borrowings, built with **FastAPI**, **PostgreSQL**, **Flyway** (database migrations), and **Docker Compose**.

## Directory structure

```
project/
├── app/
│   ├── main.py              # FastAPI application entry point
│   ├── database.py          # SQLAlchemy engine & session factory
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── models/
│   │   ├── __init__.py
│   │   ├── book.py          # Book ORM model
│   │   └── borrowing.py     # Borrowing ORM model
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── book.py          # Pydantic schemas for Book
│   │   └── borrowing.py     # Pydantic schemas for Borrowing
│   └── routers/
│       ├── __init__.py
│       ├── books.py         # CRUD endpoints for /books
│       └── borrowings.py    # CRUD endpoints for /borrowings
├── db/
│   └── migrations/
│       ├── V1__create_books_table.sql
│       └── V2__create_borrowings_table.sql
├── docker-compose.yml
├── .env
└── README.md
```

## Services

| Service  | Description                                    |
|----------|------------------------------------------------|
| `db`     | PostgreSQL 16 database                         |
| `flyway` | Runs Flyway migrations on startup              |
| `app`    | FastAPI app served with Uvicorn on port 8000   |

## Quick start

```bash
cp .env.example .env   # adjust credentials if needed
docker compose up --build
```

API docs are available at <http://localhost:8000/docs>.

## API endpoints

### Books

| Method | Path            | Description          |
|--------|-----------------|----------------------|
| GET    | /books          | List all books       |
| GET    | /books/{id}     | Get a single book    |
| POST   | /books          | Create a book        |
| DELETE | /books/{id}     | Delete a book        |

### Borrowings

| Method | Path                        | Description             |
|--------|-----------------------------|-------------------------|
| GET    | /borrowings                 | List all borrowings     |
| GET    | /borrowings/{id}            | Get a single borrowing  |
| POST   | /borrowings                 | Create a borrowing      |
| PATCH  | /borrowings/{id}/return     | Mark book as returned   |
