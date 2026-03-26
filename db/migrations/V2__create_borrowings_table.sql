CREATE TABLE IF NOT EXISTS borrowings (
    id            SERIAL PRIMARY KEY,
    book_id       INTEGER     NOT NULL REFERENCES books(id),
    borrower_name VARCHAR(255) NOT NULL,
    borrowed_at   DATE        NOT NULL,
    returned_at   DATE
);
