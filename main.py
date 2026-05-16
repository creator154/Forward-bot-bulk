import asyncio
import os

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message

# =========================
# CONFIG
# =========================

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# =========================
# BOT CLIENT
# =========================

app = Client(
    "forward-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# =========================
# START COMMAND
# =========================

@app.on_message(filters.command("start"))
async def start(_, message: Message):

    text = (
        "✅ Forward Bot Active\n\n"
        "📌 Command:\n"
        "/clone @source @destination\n\n"
        "Example:\n"
        "/clone @channel1 @channel2"
    )

    await message.reply_text(text)

# =========================
# CLONE COMMAND
# =========================

@app.on_message(filters.command("clone"))
async def clone(_, message: Message):

    args = message.text.split()

    if len(args) != 3:
        return await message.reply_text(
            "❌ Usage:\n"
            "/clone @source @destination"
        )

    source = args[1]
    destination = args[2]

    status = await message.reply_text(
        "🚀 Cloning Started..."
    )

    copied = 0
    failed = 0

    try:

        async for msg in app.get_chat_history(source):

            try:

                if msg.empty:
                    continue

                await app.copy_message(
                    chat_id=destination,
                    from_chat_id=source,
                    message_id=msg.id
                )

                copied += 1

                # Progress Update
                if copied % 20 == 0:

                    await status.edit_text(
                        f"🚀 Cloning Running...\n\n"
                        f"📦 Copied : {copied}\n"
                        f"❌ Failed : {failed}"
                    )

                # Anti Flood
                await asyncio.sleep(1)

            except FloodWait as e:

                wait_time = int(e.value)

                await status.edit_text(
                    f"⏳ FloodWait Detected\n\n"
                    f"Waiting {wait_time} seconds..."
                )

                await asyncio.sleep(wait_time)

            except Exception as err:

                failed += 1
                print(f"ERROR : {err}")

        await status.edit_text(
            f"✅ Cloning Completed\n\n"
            f"📦 Total Copied : {copied}\n"
            f"❌ Failed : {failed}"
        )

    except Exception as e:

        await status.edit_text(
            f"❌ Error:\n\n{e}"
        )

# =========================
# RUN BOT
# =========================

print("✅ Bot Started Successfully...")
app.run()
