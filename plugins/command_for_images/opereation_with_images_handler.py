from pyrogram import Client, filters
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import pillow_lut
import os

@Client.on_message(filters.command(["get_all_images"]) & filters.me)
async def send_all_images(client, message):
    all_images_filename = os.listdir("./images")
    for filename in all_images_filename:
        await client.send_photo(message.chat.id, "./images/" + filename, caption=filename)
    await message.delete()


@Client.on_message(filters.photo & filters.me)
async def add_photo(client, message):
    if message.caption.startswith("/add_photo"):
        filename = message.caption.split(" ")[1]
        await client.download_media(message, file_name="./images/" + filename)
        await client.send_message("me", filename)

@Client.on_message(filters.command(["remove_image"]) & filters.me)
async def remove_image(client, message):
    filename = message.text.split(" ")[1]
    os.remove("./images/" + filename)

# @Client.on_message(filters.me & filters.command(["add_filter"]))
# async def add_filter(client, message):
#     settings = message.text.split("\n")
#     photo = Image.open("./images/" + settings[1])
#     lut =  pillow_lut.load_cube_file("./filters/cube/test/warm.cube")
#     # lut = ImageFilter.Color3DLUT.generate()
#     photo.filter(lut).save("images/newFIlter.jpg")

@Client.on_message(filters.document & filters.me)
async def add_filter(client, message):
    if message.caption.startswith("/add_filter"):
        filename = message.caption.split(" ")[1]
        await client.download_media(message, file_name="./filters/" + filename)
