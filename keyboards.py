from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton,InlineKeyboardMarkup


btn_bad = InlineKeyboardButton("КАЛЛ 🤮", callback_data='bt2')
btn_cool = InlineKeyboardButton("КЛАСС 😎", callback_data='bt1')
greet_kb = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(btn_cool, btn_bad)

btn_black = InlineKeyboardButton("⬛", callback_data='c#000000')
btn_wight = InlineKeyboardButton("⬜", callback_data='c#FFFFFF')
btn_green = InlineKeyboardButton("🟩", callback_data='c#00FF00')
btn_yellow = InlineKeyboardButton("🟨", callback_data='c#FFFF00')
btn_red = InlineKeyboardButton("🟥", callback_data='c#FF0000')
btn_blue = InlineKeyboardButton("🟦", callback_data='c#0000FF')

c_kb = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(btn_black, btn_wight, btn_green, btn_yellow, btn_red, btn_blue)

l1= InlineKeyboardButton("в чёрной рамке", callback_data='l1')
l2= InlineKeyboardButton("с рандомным фильтром", callback_data='l2')
l3= InlineKeyboardButton("пикселизация", callback_data='l3')
l4= InlineKeyboardButton("trigered", callback_data='l4')
l5= InlineKeyboardButton("2 строки", callback_data='l5')
l6= InlineKeyboardButton("moshu", callback_data='l6')
l7= InlineKeyboardButton("искажение 😂", callback_data='l7')
l8= InlineKeyboardButton("наложение", callback_data='l8')
l9= InlineKeyboardButton("сжатие", callback_data='l9')
l10= InlineKeyboardButton("усики", callback_data='l10')
l11= InlineKeyboardButton("очки", callback_data='l11')
l_kb = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2).add(l1,l3).add(l2).add(l4).add(l5, l6).add(l7).add(l8, l9).add(l10, l11)



m1= InlineKeyboardButton("слева", callback_data='m1')
m2= InlineKeyboardButton("справа", callback_data='m2')

moshu_kb = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2).add(m1,m2)

q1= InlineKeyboardButton("высокий", callback_data='q1')
q2= InlineKeyboardButton("широкий", callback_data='q2')

szg_kb = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2).add(q1,q2)