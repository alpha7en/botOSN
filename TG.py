import config
import ttt
import szg
import moshu_generator as mg
import trigered as tr
import pixelate
import iskaz
import nalozg
import blackFON
import filterPIL
import os
import draw
import stalin_mainusi
import keyboards as kb
import lines
from aiogram import Bot, Dispatcher, executor, types
import logging
from sqlitecontrol import Sqlitecontrol
logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)
db = Sqlitecontrol('TGBase.db')
#определение




@dp.callback_query_handler(lambda c: c.data and c.data.startswith('bt'))
async def process_callback_bt_cool(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    await bot.answer_callback_query(callback_query.id)
    if code.isdigit():
        code = int(code)
    if db.obr_get(callback_query.from_user.id)==1:
        if code == 1:


            markup1 = types.ReplyKeyboardRemove()
            await bot.send_message(callback_query.from_user.id, 'Нажата крутая кнопка!')
            db.obr_set(callback_query.from_user.id, 0)
            db.like_set(callback_query.from_user.id, 1)
        elif code == 2:



            markup1 = types.ReplyKeyboardRemove()
            await bot.send_message(callback_query.from_user.id, 'Нажата грустная кнопка!')
            db.obr_set(callback_query.from_user.id, 0)
            db.like_set(callback_query.from_user.id, -1)
    else:
        await bot.send_message(callback_query.from_user.id, 'Асуждаю двойные нажатия!')





@dp.callback_query_handler(lambda c: c.data and c.data.startswith('c'))
async def process_callback_l(callback_query: types.CallbackQuery):
    code = callback_query.data[1:]
    await bot.answer_callback_query(callback_query.id)
    if db.status_get(callback_query.from_user.id) == 2:
        await bot.delete_message(callback_query.from_user.id, int(db.get_args(callback_query.from_user.id)[3]))

        markup1 = types.ReplyKeyboardRemove()
        db.status_set(callback_query.from_user.id, 3)
        db.set_args(callback_query.from_user.id, 1, code)
        mas = db.get_args(callback_query.from_user.id)
        filterPIL.filter(str(callback_query.from_user.id) + '.jpg')
        draw.dr((str(callback_query.from_user.id) + '.jpg'), db.get_name(callback_query.from_user.id), mas)
        f = open(str(callback_query.from_user.id) + '.jpg', "rb")
        await Bot.send_photo(self=bot, chat_id=callback_query.from_user.id, photo=f)

        await bot.send_message(callback_query.from_user.id, 'ну как?', reply_markup=kb.greet_kb)
        db.obr_set(callback_query.from_user.id, 1)
        os.remove(str(callback_query.from_user.id) + '.jpg')
        # await bot.send_photo(message.from_user.id, im)
    elif(db.status_get(callback_query.from_user.id) == 30):
        db.set_args(callback_query.from_user.id, 1, code)
        await bot.send_message(callback_query.from_user.id, "введи текст верхней строки 👽")
        db.status_set(callback_query.from_user.id, 31)
    else:
        await bot.send_message(callback_query.from_user.id, 'Асуждаю ненужные нажатия!')

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('l'))
async def process_callback_c(callback_query: types.CallbackQuery):
    code = callback_query.data[1:]
    await bot.answer_callback_query(callback_query.id)
    if code == '2':
        await bot.send_message(callback_query.from_user.id, "введи размер подписи\n(0 если не нужна)\n(рекомендую 50)")
        db.status_set(callback_query.from_user.id, 1)
    elif code == '1':
        await bot.send_message(callback_query.from_user.id, "введи слово")
        db.status_set(callback_query.from_user.id, 10)
    elif code == '3':
        await bot.send_message(callback_query.from_user.id, "введи степень пикселизации (попробуй 16) 🦍")
        db.status_set(callback_query.from_user.id, 20)
    elif code == '4':
        tr.r(str(callback_query.from_user.id) + '.jpg')
        f = open(str(callback_query.from_user.id) + '.jpg', "rb")
        await bot.send_photo( callback_query.from_user.id, photo=f)
        os.remove(str(callback_query.from_user.id) + '.jpg')
        await bot.delete_message(callback_query.from_user.id, int(db.get_args(callback_query.from_user.id)[3]))
        await bot.send_message(callback_query.from_user.id, 'ну как?', reply_markup=kb.greet_kb)
        db.obr_set(callback_query.from_user.id, 1)
    elif code == '5':
        db.status_set(callback_query.from_user.id, 30)
        await bot.send_message(callback_query.from_user.id, 'какой цвет подписи?', reply_markup=kb.c_kb)
    elif code == '6':
        await bot.send_message(callback_query.from_user.id, 'слева или справа?', reply_markup=kb.moshu_kb)
    elif code == '7':
        iskaz.r(str(callback_query.from_user.id) + '.jpg')
        f = open(str(callback_query.from_user.id) + '.jpg', "rb")
        await bot.send_photo( callback_query.from_user.id, photo=f)
        os.remove(str(callback_query.from_user.id) + '.jpg')
        await bot.delete_message(callback_query.from_user.id, int(db.get_args(callback_query.from_user.id)[3]))
        await bot.send_message(callback_query.from_user.id, 'как по мне полный рофл, а тебе как?', reply_markup=kb.greet_kb)
        db.obr_set(callback_query.from_user.id, 1)
    elif code == '8':
        db.status_set(callback_query.from_user.id, 45)
        await bot.delete_message(callback_query.from_user.id, int(db.get_args(callback_query.from_user.id)[3]))
        await bot.send_message(callback_query.from_user.id, 'а что сверху?')
    elif code == '9':
        db.obr_set(callback_query.from_user.id, 50)
        await bot.send_message(callback_query.from_user.id, 'kak delaem?', reply_markup=kb.szg_kb)
    elif code == '10':
        stalin_mainusi.doFace(str(callback_query.from_user.id) + '.jpg')
        f = open(str(callback_query.from_user.id) + '.jpg', "rb")
        await bot.send_photo(callback_query.from_user.id, photo=f)
        os.remove(str(callback_query.from_user.id) + '.jpg')
        await bot.delete_message(callback_query.from_user.id, int(db.get_args(callback_query.from_user.id)[3]))
        await bot.send_message(callback_query.from_user.id, 'как по мне полный рофл, а тебе как?',
                               reply_markup=kb.greet_kb)
        db.obr_set(callback_query.from_user.id, 1)
    elif code == '11':
        await bot.send_message(callback_query.from_user.id, "введи коэффициенты поиска чем больше лицо на фото, тем больше коэффициент(любое число от 1 до 10, если совсем никакк пробуй 1.01 и через пробел другое уже целое, от 1 до 50) ")
        db.status_set(callback_query.from_user.id, 60)



    #await bot.edit_message_reply_markup(callback_query.id, message_id = callback_query.message.message_id-1, reply_markup = '')
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('q'))
async def szg_otvet(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    code = callback_query.data[1:]
    if code == '1':
        szg.r(str(callback_query.from_user.id) + '.jpg', 1)
        f = open(str(callback_query.from_user.id) + '.jpg', "rb")
        await bot.send_photo( callback_query.from_user.id, photo=f)
        os.remove(str(callback_query.from_user.id) + '.jpg')
        await bot.delete_message(callback_query.from_user.id, int(db.get_args(callback_query.from_user.id)[3]))
        await bot.send_message(callback_query.from_user.id, 'nycho?', reply_markup=kb.greet_kb)
        db.obr_set(callback_query.from_user.id, 1)
    else:
        szg.r(str(callback_query.from_user.id) + '.jpg', 2)
        f = open(str(callback_query.from_user.id) + '.jpg', "rb")
        await bot.send_photo( callback_query.from_user.id, photo=f)
        os.remove(str(callback_query.from_user.id) + '.jpg')
        await bot.delete_message(callback_query.from_user.id, int(db.get_args(callback_query.from_user.id)[3]))
        await bot.send_message(callback_query.from_user.id, 'nycho?', reply_markup=kb.greet_kb)
        db.obr_set(callback_query.from_user.id, 1)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('m'))
async def process_callback_c(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    code = callback_query.data[1:]
    if code == '1':
        mg.r(str(callback_query.from_user.id) + '.jpg', True)
        f = open(str(callback_query.from_user.id) + '.jpg', "rb")
        await bot.send_photo( callback_query.from_user.id, photo=f)
        os.remove(str(callback_query.from_user.id) + '.jpg')
        await bot.delete_message(callback_query.from_user.id, int(db.get_args(callback_query.from_user.id)[3]))
        await bot.send_message(callback_query.from_user.id, 'ну как?', reply_markup=kb.greet_kb)
        db.obr_set(callback_query.from_user.id, 1)
    else:
        mg.r(str(callback_query.from_user.id) + '.jpg')
        f = open(str(callback_query.from_user.id) + '.jpg', "rb")
        await bot.send_photo( callback_query.from_user.id, photo=f)
        os.remove(str(callback_query.from_user.id) + '.jpg')
        await bot.delete_message(callback_query.from_user.id, int(db.get_args(callback_query.from_user.id)[3]))
        await bot.send_message(callback_query.from_user.id, 'ну как?', reply_markup=kb.greet_kb)
        db.obr_set(callback_query.from_user.id, 1)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markdown = """
            *bold text*
            _italic text_
            [text](URL)
            """
    await message.answer("*Привет*. Я посмогу тебе создавать классные мемы *без всяких усилий.*\n напиши мне своё имя для подписи.\n вот так: setname (имя)\n Затем можете отправлять своё фото для мема и выбирать режимы\n напиши /myrate для просмотра ваше рейтинга *оценки* моей работы \n \n [мой канал](https://www.youtube.com/channel/UCMBxOvbDi8qN81yT8NmmeXw) \nнапиши /rename _(имя)_ и *смени* своё имя\n [написать мне](t.me/@Alpha7en)", parse_mode="Markdown")

@dp.message_handler(commands=['printfall'])
async def start(message: types.Message):
    await message.answer(db.printf())


@dp.message_handler(commands=['myrate'])
async def my_rate(message: types.Message):
    markdown = """
        *bold text*
        _italic text_
        [text](URL)
        """
    await message.answer(('_ваш счёт:_  *' + str(db.like_get(message.from_user.id)) + '*'),parse_mode="Markdown")

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    db.status_set(message.from_user['id'],0)
    markdown = """
                *bold text*
                _italic text_
                [text](URL)
                """
    await message.answer("*Привет*. Я посмогу тебе создавать классные мемы _без всяких усилий._\n напиши мне своё имя для подписи.\n вот так: /setname ( +имя) \nЗатем можете отправлять своё фото для мема\n напиши /myrate для просмотра ваше рейтинга _оценки_ моей работы \n \n [мой канал](https://www.youtube.com/channel/UCMBxOvbDi8qN81yT8NmmeXw) \n [написать мне](t.me/@Alpha7en)", parse_mode="Markdown")


@dp.message_handler(commands=['rename'])
async def help(message: types.Message):
    db.status_set(message.from_user['id'],0)
    markdown = """
                *bold text*
                _italic text_
                [text](URL)
               """



    if db.get_args(message.from_user['id'])[2] == '1':

        db.set_name(tg_id=message.from_user['id'], name=message.get_args())
        await message.answer("*zapomnil*", parse_mode="Markdown")
    else:
        await message.answer("*решил имечко сменить?* я загадал число _просто напиши мне его_ и сможешь менять имя", parse_mode="Markdown")
        db.status_set(message.from_user['id'],39)


@dp.message_handler(commands=['setname'])
async def set_name(message: types.Message):
    print(message.from_user['id'])
    print(message.get_args())
    if message.get_args() == '' or None:
        await message.answer("эммм. Пусто как-бы!")
    elif(db.exists(message.from_user['id']) == None):
        db.add_name(tg_id=message.from_user['id'], name=message.get_args())
        await message.answer("я тебя запомню, можешь скинуть фото")
    else:
        await message.answer("эммм, я тебя и так знаю, но если хочешь сменить имя просто напиши /rename")

@dp.message_handler(content_types=['photo'])
async def photoes(message):
    if(db.exists(message.from_user['id']) == None):
        await message.answer("АСУЖДАЮ, может имя введешь? \n setname (имя)")
    else:
        try:
            os.remove(str(callback_query.from_user.id) + '.jpg')
        except:
            pass
        if db.status_get(message.from_user['id']) ==45:
            await message.photo[-1].download(str(message.from_user['id'])+'v.jpg')
            nalozg.r(str(message.from_user['id'])+'.jpg')
            f = open(str(message.from_user['id']) + '.jpg', "rb")
            await Bot.send_photo(self=bot, chat_id=message.from_user['id'], photo=f)
            os.remove(str(message.from_user['id']) + '.jpg')
            db.status_set(message.from_user['id'],0)
            await bot.send_message(message.from_user['id'], 'ну как?', reply_markup=kb.greet_kb)
            db.obr_set(message.from_user['id'], 1)
            db.status_set(message.from_user['id'],0)
        else:
            await message.photo[-1].download(str(message.from_user['id'])+'.jpg')
            message_info = await message.answer("выбери режим:", reply_markup=kb.l_kb)
            db.set_args(message.from_user['id'], 3, message_info['message_id'])

@dp.message_handler(content_types=['text'])
async def all_mess(message):
    if db.status_get(message.from_user['id']) == 60:
        try:
            e = message.text.split()
            k2 = int(e[1])
            k1 = float(e[0])
            if k1 <= 1.0001:
                k1 = 1.5
            if k2 > 50:
                k2 = 50
            ttt.doFace(str(message.from_user['id']) + '.jpg', k1, k2)
            f = open(str(message.from_user['id']) + '.jpg', "rb")
            await bot.send_photo(message.from_user['id'], photo=f)
            os.remove(str(message.from_user['id']) + '.jpg')
            await bot.delete_message(message.from_user['id'], int(db.get_args(message.from_user['id'])[3]))
            await bot.send_message(message.from_user['id'], 'как по мне полный рофл, а тебе как?',
                                   reply_markup=kb.greet_kb)
            db.obr_set(message.from_user['id'], 1)
        except:
            await bot.send_message(message.from_user['id'], 'Нет, ну что за человек? НОРМАЛЬНЫЕ ЧИСЛА ВВОДИ!')


    if db.status_get(message.from_user['id']) == 39:
        var = ("асуждаю", "осуждаю", "Асуждаю", "Осуждаю","асуждаю!", "осуждаю!", "Асуждаю!", "Осуждаю!")
        if message.text in var:
            await bot.send_message(message.from_user['id'], 'СЕБЯ ОСУДИ!')
        if message.text == '39':
            await bot.send_message(message.from_user['id'], 'а ты я смотрю шаришь, или просто угадал. Разрешаю писать /rename (новое имя)')
            db.set_args(message.from_user['id'], 2, 1)

    if db.status_get(message.from_user['id']) == 1:
        try:
            it = int(message.text)
            if it != 0:
                await bot.send_message(message.from_user['id'], 'какой цвет подписи?', reply_markup=kb.c_kb)
                db.status_set(message.from_user['id'], 2)
                db.set_args(message.from_user['id'], 0,str(it))
            else:
                markup1 = types.ReplyKeyboardRemove()
                db.status_set(message.from_user['id'], 3)
                filterPIL.filter(str(message.from_user['id']) + '.jpg')

                f = open(str(message.from_user['id']) + '.jpg', "rb")
                await Bot.send_photo(self=bot, chat_id=message.from_user['id'], photo=f)
                await bot.delete_message(message.from_user['id'], int(db.get_args(message.from_user['id'])[3]))
                await bot.send_message(message.from_user['id'], 'ну как?', reply_markup=kb.greet_kb)
                db.obr_set(message.from_user['id'], 1)
                os.remove(str(message.from_user['id']) + '.jpg')


        except Exception as exc:
            await bot.send_message(message.from_user['id'], 'может число введёшь ?')
            print(exc)
    if db.status_get(message.from_user['id']) == 10:

        it = (message.text)

        blackFON.r(str(message.from_user['id']) + '.jpg', it)
        f = open(str(message.from_user['id']) + '.jpg', "rb")
        await Bot.send_photo(self=bot, chat_id=message.from_user['id'], photo=f)
        os.remove(str(message.from_user['id']) + '.jpg')
        await bot.delete_message(message.from_user['id'], int(db.get_args(message.from_user['id'])[3]))
        await bot.send_message(message.from_user['id'], 'ну как?', reply_markup=kb.greet_kb)
        db.obr_set(message.from_user['id'], 1)

    if db.status_get(message.from_user['id']) == 20:
        try:
            it = int(message.text)
            pixelate.r(str(message.from_user['id']) + '.jpg', it)
            f = open(str(message.from_user['id']) + '.jpg', "rb")
            await Bot.send_photo(self=bot, chat_id=message.from_user['id'], photo=f)
            os.remove(str(message.from_user['id']) + '.jpg')
            await bot.delete_message(message.from_user['id'], int(db.get_args(message.from_user['id'])[3]))
            await bot.send_message(message.from_user['id'], 'ну как?', reply_markup=kb.greet_kb)
            db.obr_set(message.from_user['id'], 1)


        except Exception as exc:
            await bot.send_message(message.from_user['id'], 'асуждаю! Может нормальное ЧИСЛО введёшь ?')
            print(exc)

    if db.status_get(message.from_user['id']) == 31:
        it = (message.text)
        await bot.send_message(message.from_user['id'], 'теперь нижнюю строчку')
        db.status_set(message.from_user['id'], 32)
        db.set_args(message.from_user['id'], 0, str(it))
        return
    if db.status_get(message.from_user['id']) == 32:
        it = (message.text)
        lines.generate_meme(str(message.from_user['id']) + '.jpg', db.get_args(message.from_user['id'])[0], it,  db.get_args(message.from_user['id'])[1])
        f = open(str(message.from_user['id']) + '.jpg', "rb")
        await Bot.send_photo(self=bot, chat_id=message.from_user['id'], photo=f)
        os.remove(str(message.from_user['id']) + '.jpg')
        await bot.delete_message(message.from_user['id'], int(db.get_args(message.from_user['id'])[3]))
        await bot.send_message(message.from_user['id'], 'ну как?', reply_markup=kb.greet_kb)
        db.obr_set(message.from_user['id'], 1)

if __name__ == '__main__':
    mode = 0
    if mode == 1:
        try:
            executor.start_polling(dp, skip_updates=True)
        except:
            pass
    else:
        executor.start_polling(dp, skip_updates=True)