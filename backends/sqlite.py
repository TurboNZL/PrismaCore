import sqlite3
import asyncio
import os

DB_PATH = os.getenv("SQLITE_PATH", "prisma.db")

async def query(table, filters, columns):
    """sqlite query that returns a list of dicts (a queried table)"""
    def _blocking():
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row  # lets you access columns by name
        cursor = conn.cursor() # what is currently selected

        cols = ", ".join(columns) if columns else "*" # formats colums in sqlite lang
        sql = f"SELECT {cols} FROM {table}" # an f string for sqlite lang

        if filters:
            conditions = " AND ".join(f"{k} = ?" for k in filters) # joins all conditions with AND
            sql += f" WHERE {conditions}" # Makes it WHERE this AND that
            cursor.execute(sql, list(filters.values())) # takes the value halves of the dicts and runs the sql against each value in the list
        else:
            cursor.execute(sql)

        rows = [dict(row) for row in cursor.fetchall()] # turns the list of rows into a list of dicts
        conn.close() # closes sqlite databse
        return rows
    return await asyncio.to_thread(_blocking)

async def upsert(table, data):
    """sqlite upsert with auto primary key detection"""
    def _blocking():
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # discover primary key(s)
        cursor.execute(f"PRAGMA table_info({table})")
        info = cursor.fetchall()
        pk_cols = [row["name"] for row in info if row["pk"] > 0]

        cols = ", ".join(data.keys())
        placeholders = ", ".join("?" for _ in data)
        conflict_target = ", ".join(pk_cols)
        updates = ", ".join(f"{k} = excluded.{k}" for k in data if k not in pk_cols)

        sql = f"""
            INSERT INTO {table} ({cols}) VALUES ({placeholders})
            ON CONFLICT ({conflict_target}) DO UPDATE SET {updates}
        """

        cursor.execute(sql, list(data.values()))
        conn.commit()
        conn.close()

    return await asyncio.to_thread(_blocking)