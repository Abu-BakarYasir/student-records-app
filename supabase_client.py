from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

Url=os.getenv("SUPABASE_URL")
key=os.getenv("SUPABASE_KEY")

supabase=create_client(Url,key)

