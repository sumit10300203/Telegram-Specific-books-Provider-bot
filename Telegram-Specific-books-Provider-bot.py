import asyncio
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, ForceReply

bot_token = "Enter your bot token here"
bot = Client(str("App Name"), api_id = int("Your api_id"), api_hash = str("Your api hash"), bot_token = bot_token)
myself = int("your user_id in telegram")

def mine(filter, bot, Message):
    if int(myself) == Message.chat.id:
        return 1
    return 0

START_MESSAGE_BUTTONS_0 = [
    [InlineKeyboardButton(text = "CSE", callback_data = "CSE"), InlineKeyboardButton(text = "EE", callback_data = "EE"), InlineKeyboardButton(text = "CE", callback_data = "CE")]
]

@bot.on_message(filters.command("start") & filters.private)
async def start(bot, message):
    reply_markup = InlineKeyboardMarkup(START_MESSAGE_BUTTONS_0)
    await bot.send_message(message.chat.id, f"Hello {message.chat.first_name}, Myself Makaut Organizer Provider Bot, currently i can provide you 5th sem CSE, EE, CE 2022 Organizer", reply_markup = reply_markup, parse_mode=enums.ParseMode.MARKDOWN)

START_MESSAGE_BUTTONS_1 = [
    [InlineKeyboardButton(text = "Reply", callback_data = "Reply")]
]

@bot.on_message(filters.private & ~(filters.create(func = mine)))
async def send(bot, message):
    if message.text != None:
        reply_markup = InlineKeyboardMarkup(START_MESSAGE_BUTTONS_1)
        await bot.send_message(myself, f"||{message.chat.id}||\n@{message.chat.username}\n{message.chat.first_name} - {message.text}", disable_notification = 1, reply_markup = reply_markup, disable_web_page_preview = 1, parse_mode=enums.ParseMode.MARKDOWN)

@bot.on_callback_query()
async def callback_query(bot, CallbackQuery):
    try:
        if CallbackQuery.data == "Reply":
            reply_to_message_id = CallbackQuery.message.id
            await bot.send_message(myself, "Enter your reply here", reply_to_message_id = reply_to_message_id, reply_markup = ForceReply(), parse_mode=enums.ParseMode.MARKDOWN)
    except:
        await bot.send_message(myself, "Error Sending Message")
    try:
        if CallbackQuery.data == "CSE":
            await bot.send_document(CallbackQuery.from_user.id, str("Document id"), caption = "Industrial Management", force_document  = 1, protect_content = 1)
            await bot.send_document(CallbackQuery.from_user.id, str("Document id"), caption = "Compiler Design", force_document  = 1, protect_content = 1)
            await bot.send_document(CallbackQuery.from_user.id, str("Document id"), caption = "Operating System", force_document  = 1, protect_content = 1)
            await bot.send_document(CallbackQuery.from_user.id, str("Document id"), caption = "Software Engineering", force_document  = 1, protect_content = 1)
            await bot.send_document(CallbackQuery.from_user.id, str("Document id"), caption = "Object Oriented Programming", force_document  = 1, protect_content = 1)
            await bot.send_document(CallbackQuery.from_user.id, str("Document id"), caption = "Artificial Intelligence", force_document  = 1, protect_content = 1)
            await bot.send_message(CallbackQuery.from_user.id, "Help your friends by sharing me \nt.me/makautorganizerprovider2022bot\n(CSE, EE, CE Organizers available)\n\nThis @makautorganizerprovider2022bot bot will be stopped after 28th Nov as **Heroku** will stop their free services, it is recommended to use this bot asap to users, if possible suggest me a **free hosting service like heroku**... \nThank You", parse_mode=enums.ParseMode.MARKDOWN)
            await bot.send_message(myself, f"@{CallbackQuery.from_user.username}\n{CallbackQuery.from_user.first_name} used bot (CSE)", disable_notification = 1)
        elif CallbackQuery.data == "EE":
            await bot.send_document(CallbackQuery.from_user.id, str("Document id"), caption = "ORGANIZER_ POWER SYSTEM - I EE-5TH-Sem", force_document  = 1, protect_content = 1)
            await bot.send_document(CallbackQuery.from_user.id, str("Document id"), caption = "ORGANIZER_DATA STRUCTURE &_ALGORITHM-EE-5TH-Sem", force_document  = 1, protect_content = 1)
            await bot.send_document(CallbackQuery.from_user.id, str("Document id"), caption = "ORGANIZER_POWER ELECTRONICS-5th-sem-EE", force_document  = 1, protect_content = 1)
            await bot.send_document(CallbackQuery.from_user.id, str("Document id"), caption = "ORGANIZER-CONTROL-SYSTEM-EE-5TH-Sem", force_document  = 1, protect_content = 1)
            await bot.send_document(CallbackQuery.from_user.id, str("Document id"), caption = "ORGANIZER-MACHINE - II EE-5TH-Sem", force_document  = 1, protect_content = 1)
            await bot.send_document(CallbackQuery.from_user.id, str("Document id"), caption = "ORGANIZER-RENEWABLE-&-NON-CONVENTIONAL-EE-5TH-Sem", force_document  = 1, protect_content = 1)
            await bot.send_message(CallbackQuery.from_user.id, "Help your friends by sharing me \nt.me/makautorganizerprovider2022bot\n(CSE, EE, CE Organizers available)\n\nThis @makautorganizerprovider2022bot bot will be stopped after 28th Nov as **Heroku** will stop their free services, it is recommended to use this bot asap to users, if possible suggest me a **free hosting service like heroku**... \nThank You", parse_mode=enums.ParseMode.MARKDOWN)
            await bot.send_message(myself, f"@{CallbackQuery.from_user.username}\n{CallbackQuery.from_user.first_name} used bot (EE)", disable_notification = 1)
        elif CallbackQuery.data == "CE":
            await bot.send_document(CallbackQuery.from_user.id, str("Document id"), caption = "All in one PDF", force_document  = 1, protect_content = 1)
            await bot.send_message(CallbackQuery.from_user.id, "Help your friends by sharing me \nt.me/makautorganizerprovider2022bot\n(CSE, EE, CE Organizers available)\n\nThis @makautorganizerprovider2022bot bot will be stopped after 28th Nov as **Heroku** will stop their free services, it is recommended to use this bot asap to users, if possible suggest me a **free hosting service like heroku**... \nThank You", parse_mode=enums.ParseMode.MARKDOWN)
            await bot.send_message(myself, f"@{CallbackQuery.from_user.username}\n{CallbackQuery.from_user.first_name} used bot (CE)", disable_notification = 1)
    except:
        pass

@bot.on_message(filters.reply & filters.private & filters.create(func = mine))
async def reply(bot, message):
    try:
        res = await bot.get_messages(myself, message.reply_to_message_id)
        ID = res.reply_to_message.text.split('\n')[0]
        await bot.send_message(ID, message.text, parse_mode=enums.ParseMode.MARKDOWN)
    except:
        await bot.send_message(myself, "Error Sending Message")

bot.run()
