from pyrogram import Client, filters
from PIL import Image, ImageDraw, ImageFont
import os

@Client.on_message(filters.command(["send_mem"]) & filters.me)
async def send_mem(client, message):
    mem_name = message.text.split("\n")[1]
    await client.send_photo(message.chat.id, "mems/" + mem_name + ".jpg") 

@Client.on_message(filters.command(["create_mem"]) & filters.me)
async def send_test_photo(client, message):
    text_of_message = message.text.split("\n")
    font = ImageFont.truetype("fonts/Roboto-Black.ttf", int(text_of_message[5]))
    im = Image.open("images/" + text_of_message[6])
    draw = ImageDraw.Draw(im)
    draw.multiline_text((int(text_of_message[2]), int(text_of_message[3])), text_of_message[1], font=font, fill=text_of_message[4])
    im.save("mems/" + text_of_message[7])
    await client.send_photo(message.chat.id, "mems/" + text_of_message[7])
    await message.delete()

@Client.on_message(filters.command(["get_all_mems"]) & filters.me)
async def send_all_mems(client, message):
    all_images_filename = os.listdir("./mems")
    for filename in all_images_filename:
        await client.send_photo(message.chat.id, "./mems/" + filename, caption=filename)
    await message.delete()

@Client.on_message(filters.command(["remove_mem"]) & filters.me)
async def remove_mem(client, message):
    filename = message.text.split(" ")[1]
    os.remove("./mems/" + filename)