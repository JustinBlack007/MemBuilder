from pyrogram import Client, filters

@Client.on_message(filters.command(["clear"]))
async def clear_messages(client, message):
    text_of_message = message.text.split(" ")
    all_messages = await client.get_history(message.chat.id, limit=int(text_of_message[1]) + 1)
    await message.delete()
    for on_message in all_messages:
        await on_message.delete()

@Client.on_message(filters.command(["help"]) & filters.me)
async def send_help_message(client, message):
    await client.send_message(message.chat.id, "test")

@Client.on_message(filters.command(["test"]))
async def test_text(client, message):
    await client.send_message("me", "test")