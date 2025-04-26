import logging
import os
import aiosqlite
import asyncio
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command

load_dotenv()


TOKEN = os.getenv("TOKEN")

dp = Dispatcher()



@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("qq")


@dp.message(Command("create"))
async def create(message: Message):
    
    chat_id = message.chat.id
    note = message.text[8:].strip()
    note_id = None
    async with aiosqlite.connect("main.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                chat_id INTEGER,
                note_id INTEGER PRIMARY KEY AUTOINCREMENT,
                note TEXT
            )
            """)    
        await db.commit()
    
    
    async with aiosqlite.connect("main.db") as db:
        
        await db.execute("""
            INSERT INTO notes (chat_id, note) VALUES (?, ?)
            """, (chat_id, note))   
        
        
        cursor = await db.execute("SELECT last_insert_rowid()")
        note_id = await cursor.fetchone()
        note_id = note_id[0] 
        await db.commit()
        
    await message.answer(f"Succes created: note: {note}, ID: {note_id}")


@dp.message(Command("delete"))
async def delete(message: Message):
    chat_id = message.chat.id
    #note id
    note_id = int(message.text[8:].strip())
    
    async with aiosqlite.connect("main.db") as db:
        cursor = await db.execute("""
        SELECT note_id FROM notes WHERE chat_id = ?
        """, (chat_id,))
        
        notes = await cursor.fetchall()
    
    
        if any(note_id == note[0] for note in notes):
            await db.execute(
                """DELETE FROM notes WHERE chat_id = ? AND note_id = ?"""
            , (chat_id, note_id))
            await message.answer(f"Succes deleted ID: {note_id}")
            await db.commit()
        else:
            await message.answer("Note no found")
    
@dp.message(Command("notes"))
async def notes(message: Message):
    chat_id = message.chat.id

    async with aiosqlite.connect("main.db") as db:
        cursor = await db.execute("""
        SELECT note_id, note FROM notes WHERE chat_id = ?
        """, (chat_id,))
        
        notes = await cursor.fetchall()
        
        if notes:
            notes_text = "\n".join([f"Note {note_id}: {note}" for note_id, note in notes])
            await message.answer(f"Notes:\n{notes_text}")
        else:
            await message.answer("Not found")
    
async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)
    
    
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format=("%(asctime)s - %(levelname)s - %(message)s"), handlers=[logging.FileHandler("bot.log", encoding="utf-8"), logging.StreamHandler()])
    asyncio.run(main())