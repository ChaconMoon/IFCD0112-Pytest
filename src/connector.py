from models import User
import sqlite3
class UserCRUDSQLite:
    """CRUD muy simple para SQLite orientado a ejemplos."""

    def __init__(self, db_path: str = "users.db"):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def init_db(self):
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                )
                """
            )
            conn.commit()

    def create_user(self, username: str, email: str, password: str) -> int:
        # Reutiliza validaciones de la entidad User.
        User(username, email, password)
        with self._connect() as conn:
            cursor = conn.execute(
                "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                (username, email, password),
            )
            conn.commit()
            if cursor.lastrowid is None:
                raise RuntimeError("No se pudo obtener el id insertado")
            return int(cursor.lastrowid)

    def get_user_by_id(self, user_id: int):
        with self._connect() as conn:
            row = conn.execute(
                "SELECT id, username, email, password FROM users WHERE id = ?",
                (user_id,),
            ).fetchone()

        if not row:
            return None

        return {
            "id": row[0],
            "username": row[1],
            "email": row[2],
            "password": row[3],
        }

    def list_users(self):
        with self._connect() as conn:
            rows = conn.execute(
                "SELECT id, username, email, password FROM users ORDER BY id"
            ).fetchall()

        return [
            {
                "id": row[0],
                "username": row[1],
                "email": row[2],
                "password": row[3],
            }
            for row in rows
        ]

    def update_user(self, user_id: int, username: str, email: str, password: str) -> bool:
        # Revalida datos antes de actualizar.
        User(username, email, password)
        with self._connect() as conn:
            cursor = conn.execute(
                """
                UPDATE users
                SET username = ?, email = ?, password = ?
                WHERE id = ?
                """,
                (username, email, password, user_id),
            )
            conn.commit()
            return cursor.rowcount > 0

    def delete_user(self, user_id: int) -> bool:
        with self._connect() as conn:
            cursor = conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
            conn.commit()
            return cursor.rowcount > 0

