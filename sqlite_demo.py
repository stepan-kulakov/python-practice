import sqlite3

SAMPLE_BOOKS = [
    ("Dune", "Frank Herbert", 1965),
    ("Neuromancer", "William Gibson", 1984),
    ("Foundation", "Isaac Asimov", 1951),
    ("I, Robot", "Isaac Asimov", 1950),
]


def connect() -> sqlite3.Connection:
    """Open an in-memory database whose rows can be read by column name."""
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    return conn


def create_table(conn: sqlite3.Connection) -> None:
    """Create the books table."""
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER
        )
        """
    )
    conn.commit()


def add_book(conn: sqlite3.Connection, title: str, author: str, year: int) -> None:
    """Insert one book. The ? marks are filled in safely by sqlite3."""
    conn.execute(
        "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
        (title, author, year),
    )
    conn.commit()


def list_books(conn: sqlite3.Connection) -> list[sqlite3.Row]:
    """Return all books, oldest first."""
    return conn.execute(
        "SELECT id, title, author, year FROM books ORDER BY year"
    ).fetchall()


def find_by_author(conn: sqlite3.Connection, author: str) -> list[sqlite3.Row]:
    """Return the books of one author, oldest first."""
    return conn.execute(
        "SELECT id, title, author, year FROM books WHERE author = ? ORDER BY year",
        (author,),
    ).fetchall()


def count_books(conn: sqlite3.Connection) -> int:
    """Return how many books are stored."""
    return conn.execute("SELECT COUNT(*) FROM books").fetchone()[0]


def format_book(row: sqlite3.Row) -> str:
    """Format one row as a readable line."""
    return f"{row['id']}. {row['title']} - {row['author']} ({row['year']})"


def main() -> None:
    conn = connect()
    create_table(conn)
    for title, author, year in SAMPLE_BOOKS:
        add_book(conn, title, author, year)

    print("All books:")
    for row in list_books(conn):
        print(format_book(row))

    print()
    print("Books by Isaac Asimov:")
    for row in find_by_author(conn, "Isaac Asimov"):
        print(format_book(row))

    print()
    print(f"Total books: {count_books(conn)}")
    conn.close()


if __name__ == "__main__":
    main()