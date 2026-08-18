import asyncio
from sqlalchemy import text
from app.database import engine  # Importă motorul tău din fișierul database.py

async def test_connection():
    try:
        # Încercăm să deschidem o conexiune directă
        async with engine.connect() as conn:
            # Rulăm un query simplu pentru a vedea dacă baza de date ne aude
            result = await conn.execute(text("SELECT 'Merge perfect!';"))
            print(f"✅ Conexiune reușită! Baza de date a răspuns: {result.scalar()}")
    except Exception as e:
        print(f"❌ Eroare la conectare. Detalii:\n{e}")

# Deoarece folosim o bază de date asincronă, trebuie să rulăm funcția cu asyncio
if __name__ == "__main__":
    asyncio.run(test_connection())