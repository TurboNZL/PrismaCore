import os
import importlib
from dotenv import load_dotenv

load_dotenv()

# Get the string name (e.g., "sqlite" or "supabase")
backend_name = os.getenv("DB_BACKEND")

# Dynamically import 'backends.sqlite' or 'backends.supabase'
_db = importlib.import_module(f"backends.{backend_name}")

class QueryBuilder:
    def __init__(self, table: str):
        self._table = table
        self._columns = None
        self._filters = {}

    def select(self, *columns: str):
        self._columns = list(columns)
        return self

    def where(self, **kwargs):
        self._filters.update(kwargs)
        return self

    async def execute(self):
        return await _db.query(self._table, self._filters, self._columns)


def fetch(table: str) -> QueryBuilder:
    return QueryBuilder(table)