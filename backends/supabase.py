import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Determine the Supabase schema based on the PROD_MODE environment variable
prod_mode = os.getenv("PROD_MODE", "False").lower() == "true"
if prod_mode: SUPABASE_SCHEMA = "public"
else: SUPABASE_SCHEMA = "dev"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

async def query(table, filters, columns):
    """supabase query that returns thing - unfinished"""
    def blocking():
        return (
            supabase.table(table)
            .select(columns)

        )