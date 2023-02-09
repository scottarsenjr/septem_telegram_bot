import telebot, sqlite3
from telebot import types
from config.id import button_list, shop
from config.token import bot


@bot.message_handler(commands=['start'])
def start(message):
    # Menu Appear
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    products = types.KeyboardButton(button_list['products'])
    faq = types.KeyboardButton(button_list['faq'])
    contacts = types.KeyboardButton(button_list['contacts'])

    markup.add(products, faq, contacts)

    # Greeting
    greet = f'Добро пожаловать в <b>Septem Shop</b> 🔥 <u>{message.from_user.first_name}</u>!\n'
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_animation(message.chat.id, open('media/gif/septemshopgif.gif', 'rb'), caption=greet,
                       parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def main_menu(message):
    if message.chat.type == 'private':
        # MAIN
        if message.text == button_list['products']:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            perf = types.KeyboardButton(button_list['perf'])
            comp = types.KeyboardButton(button_list['comp'])
            furn = types.KeyboardButton(button_list['furn'])
            game_device = types.KeyboardButton(button_list['game_device'])
            back = types.KeyboardButton(button_list['main_menu'])
            markup.add(perf, comp, furn, game_device, back)

            bot.send_message(message.chat.id, '📊 Выберите категорию товаров', reply_markup=markup)
            bot.send_message(message.chat.id, 'Не нашли <b>интересующего</b> вас '
                                              '<b>товара?</b>\nПишите '
                                              '<a href="https://t.me/septemshop_manager">менеджерам</a>'
                                              ' со своими предложениями'
                                              ' и мы <b>добавим ваш товар</b>',
                             reply_markup=markup, parse_mode='html', disable_web_page_preview=True)

        elif message.text == button_list['faq']:
            faq_text = f"""
❔ *Часто задаваемые вопросы*

\- Почему такие *низкие цены*?

Мы закупаем товары у *оптовых поставщиков* и размещаем обьявления с *наименьшим* процентом,
отчего стоимость товаров гораздо *ниже рыночной*\.

\- Есть ли *риск потерять деньги* и не получить товар?

Пользуясь нашими услугами вы *не рискуете* ни чем\. Процесс куплепродажи происходит в рамках популярного
в России маркетплейс\-сайта *Avito*\.

\- Что делать если ссылка на товар *не работает*?

В некоторых случаях *Avito* не позволяет нам выставлять некоторые *товары*, поэтому *если вам приглянулся
товар*, но ссылка недействительна, *просьба писать в ЛС* [менеджерам](https://t.me/septemshop_manager)

\- Можно ли где\-то *оставить отзыв*?

Отзывы о наших услугах вы можете *прочесть/оставить* на нашем [аккаунте]({shop}) маркетплейс\-сайта *Avito*\.
            """
            bot.send_message(message.chat.id, faq_text, parse_mode='MarkdownV2', disable_web_page_preview=True)

        elif message.text == button_list['contacts']:
            contact_info = """
<b>Контактная информация</b>

По всем вопросам обращаться к администраторам

@Septemshop_manager либо @septemshop_tech
            """
            bot.send_message(message.chat.id, contact_info, parse_mode='html')

        # BACK TO MENU
        elif message.text == button_list['main_menu']:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            products = types.KeyboardButton(button_list['products'])
            faq = types.KeyboardButton(button_list['faq'])
            contacts = types.KeyboardButton(button_list['contacts'])

            markup.add(products, faq, contacts)

            greet = f'Добро пожаловать в <b>Septem Shop</b> 🔥 <u>{message.from_user.first_name}</u>!\n'
            bot.send_chat_action(message.chat.id, 'typing')
            bot.send_animation(message.chat.id, open('media/gif/septemshopgif.gif', 'rb'), caption=greet,
                               parse_mode='html', reply_markup=markup)

    # PERF MENU
    if message.text == button_list['perf']:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        monitor = types.KeyboardButton(button_list['monitor'])
        # mouse = types.KeyboardButton(button_list['mouse'])
        keyboard = types.KeyboardButton(button_list['keyboard'])
        headphones = types.KeyboardButton(button_list['headphones'])
        back = types.KeyboardButton(button_list['back_product'])

        markup.add(monitor, keyboard, headphones, back)
        bot.send_message(message.chat.id, 'Выберите подкатегорию для категории "Периферия"',
                         parse_mode='html', reply_markup=markup)

    # PERF SUB-MENU
    if message.text == button_list['monitor']:
        main = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton(text=button_list['item1'], callback_data='ref/item1')
        item2 = types.InlineKeyboardButton(text=button_list['item2'], callback_data='ref/item2')
        main.add(item1, item2)
        bot.send_message(message.chat.id, 'Выберите товар из списка', reply_markup=main)

    elif message.text == button_list['keyboard']:
        main = types.InlineKeyboardMarkup(row_width=1)
        item3 = types.InlineKeyboardButton(text=button_list['item3'], callback_data='ref/item3')
        item8 = types.InlineKeyboardButton(text=button_list['item8'], callback_data='ref/item8')
        main.add(item3, item8)
        bot.send_message(message.chat.id, 'Выберите товар из списка', reply_markup=main)

    elif message.text == button_list['headphones']:
        main = types.InlineKeyboardMarkup(row_width=1)
        item23 = types.InlineKeyboardButton(text=button_list['item23'], callback_data='ref/item23')
        item24 = types.InlineKeyboardButton(text=button_list['item24'], callback_data='ref/item24')
        main.add(item23, item24)
        bot.send_message(message.chat.id, 'Выберите товар из списка', reply_markup=main)

    # COMP MENU
    if message.text == button_list['comp']:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        pc = types.KeyboardButton(button_list['pc'])
        mining = types.KeyboardButton(button_list['mining'])
        back = types.KeyboardButton(button_list['back_product'])
        markup.add(pc, mining, back)

        bot.send_message(message.chat.id, 'Выберите подкатегорию для категории "Комплектующие"',
                         parse_mode='html', reply_markup=markup)

    # COMP SUB-MENU (MINING)
    if message.text == button_list['mining']:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        motherboard = types.KeyboardButton(button_list['motherboard_mining'])
        case = types.KeyboardButton(button_list['case_mining'])
        back = types.KeyboardButton(button_list['back_product_comp'])
        markup.add(motherboard, case, back)

        bot.send_message(message.chat.id, 'Выберите подкатегорию "Комплектующие для майнинга"',
                         parse_mode='html', reply_markup=markup)

    # COMP SUB-MENU (PC)
    if message.text == button_list['pc']:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        motherboard = types.KeyboardButton(button_list['motherboard'])
        processor = types.KeyboardButton(button_list['processor'])
        videocard = types.KeyboardButton(button_list['videocard'])
        back = types.KeyboardButton(button_list['back_product_comp'])
        markup.add(motherboard, processor, videocard, back)

        bot.send_message(message.chat.id, 'Выберите подкатегорию "Комплектующие для ПК"',
                         parse_mode='html', reply_markup=markup)

    # PC SUB-MENU (COMP)
    if message.text == button_list['processor']:
        main = types.InlineKeyboardMarkup(row_width=1)
        item9 = types.InlineKeyboardButton(text=button_list['item9'], callback_data='ref/item9')
        main.add(item9)
        bot.send_message(message.chat.id, 'Выберите товар из списка', reply_markup=main)

    elif message.text == button_list['videocard']:
        main = types.InlineKeyboardMarkup(row_width=1)
        item10 = types.InlineKeyboardButton(text=button_list['item10'], callback_data='ref/item10')
        item12 = types.InlineKeyboardButton(text=button_list['item12'], callback_data='ref/item12')
        item14 = types.InlineKeyboardButton(text=button_list['item14'], callback_data='ref/item14')
        item21 = types.InlineKeyboardButton(text=button_list['item21'], callback_data='ref/item21')
        item22 = types.InlineKeyboardButton(text=button_list['item22'], callback_data='ref/item22')
        main.add(item10, item12, item14, item21, item22)
        bot.send_message(message.chat.id, 'Выберите товар из списка', reply_markup=main)

    elif message.text == button_list['motherboard']:
        main = types.InlineKeyboardMarkup(row_width=1)
        item11 = types.InlineKeyboardButton(text=button_list['item11'], callback_data='ref/item11')
        item15 = types.InlineKeyboardButton(text=button_list['item15'], callback_data='ref/item15')
        item16 = types.InlineKeyboardButton(text=button_list['item16'], callback_data='ref/item16')
        item17 = types.InlineKeyboardButton(text=button_list['item17'], callback_data='ref/item17')
        item18 = types.InlineKeyboardButton(text=button_list['item18'], callback_data='ref/item18')
        item19 = types.InlineKeyboardButton(text=button_list['item19'], callback_data='ref/item19')
        item20 = types.InlineKeyboardButton(text=button_list['item20'], callback_data='ref/item20')
        main.add(item11, item15, item16, item17, item18, item19, item20)
        bot.send_message(message.chat.id, 'Выберите товар из списка', reply_markup=main)

    # MINING SUB-MENU (COMP)
    if message.text == button_list['motherboard_mining']:
        main = types.InlineKeyboardMarkup(row_width=1)
        item4 = types.InlineKeyboardButton(text=button_list['item4'], callback_data='ref/item4')
        main.add(item4)
        bot.send_message(message.chat.id, 'Выберите товар из списка', reply_markup=main)

    elif message.text == button_list['case_mining']:
        main = types.InlineKeyboardMarkup(row_width=1)
        item5 = types.InlineKeyboardButton(text=button_list['item5'], callback_data='ref/item5')
        main.add(item5)
        bot.send_message(message.chat.id, 'Выберите товар из списка', reply_markup=main)

    # GAME DEVICE MENU
    if message.text == button_list['game_device']:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        gamepad = types.KeyboardButton(button_list['gamepad'])
        back = types.KeyboardButton(button_list['back_product'])

        markup.add(gamepad, back)
        bot.send_message(message.chat.id, 'Выберите подкатегорию для категории "Игровые устройства"',
                         parse_mode='html', reply_markup=markup)

    # GAME DEVICE SUB-MENU
    if message.text == button_list['gamepad']:
        main = types.InlineKeyboardMarkup(row_width=1)
        item6 = types.InlineKeyboardButton(text=button_list['item6'], callback_data='ref/item6')
        main.add(item6)
        bot.send_message(message.chat.id, 'Выберите товар из списка', reply_markup=main)

    # FURN MENU
    if message.text == button_list['furn']:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        chair = types.KeyboardButton(button_list['chair'])
        back = types.KeyboardButton(button_list['back_product'])
        markup.add(chair, back)

        bot.send_message(message.chat.id, '📊 Выберите категорию товаров', reply_markup=markup)

    # FURN SUB-MENU
    if message.text == button_list['chair']:
        main = types.InlineKeyboardMarkup(row_width=1)
        item7 = types.InlineKeyboardButton(text=button_list['item7'], callback_data='ref/item7')
        main.add(item7)
        bot.send_message(message.chat.id, 'Выберите товар из списка', reply_markup=main)

    # BACK BUTTON
    if message.text == button_list['back_product']:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        perf = types.KeyboardButton(button_list['perf'])
        comp = types.KeyboardButton(button_list['comp'])
        furn = types.KeyboardButton(button_list['furn'])
        game_device = types.KeyboardButton(button_list['game_device'])
        back = types.KeyboardButton(button_list['main_menu'])
        markup.add(perf, comp, furn, game_device, back)

        bot.send_message(message.chat.id, '📊 Выберите категорию товаров', reply_markup=markup)

    elif message.text == button_list['back_product_comp']:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        pc = types.KeyboardButton(button_list['pc'])
        mining = types.KeyboardButton(button_list['mining'])
        back = types.KeyboardButton(button_list['back_product'])
        markup.add(pc, mining, back)

        bot.send_message(message.chat.id, 'Выберите подкатегорию для категории "Комплектующие"',
                         parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def refs(call):
    # PERF
    # MONITOR
    if call.data == 'ref/item1':
        item_text = f'<b>{button_list["item1"]}</b>\n\n{button_list["item1_desc"]}\n\n' \
                     f'<b>Цена:</b> {button_list["item1_price"]} ₽\n\n' \
                     f'<b><a href="{button_list["item1_ref"]}">Ссылка на товар</a></b>'
        bot.send_photo(call.message.chat.id, open('media/images/perf/monitor/item1.png', 'rb'),
                       parse_mode='html', caption=item_text)
    elif call.data == 'ref/item2':
        item_text = f'<b>{button_list["item2"]}</b>\n\n{button_list["item2_desc"]}\n\n' \
                     f'<b>Цена:</b> {button_list["item2_price"]} ₽\n\n' \
                     f'<b><a href="{button_list["item2_ref"]}">Ссылка на товар</a></b>'
        bot.send_photo(call.message.chat.id, open('media/images/perf/monitor/item2.jpg', 'rb'),
                       parse_mode='html', caption=item_text)

    # KEYBOARD
    elif call.data == 'ref/item3':
        item_text = f'<b>{button_list["item3"]}</b>\n\n{button_list["item3_desc"]}\n\n' \
                     f'<b>Цена:</b> {button_list["item3_price"]} ₽\n\n' \
                     f'<b><a href="{button_list["item3_ref"]}">Ссылка на товар</a></b>'
        bot.send_photo(call.message.chat.id, open('media/images/perf/keyboard/item3.jpg', 'rb'),
                       parse_mode='html', caption=item_text)
    elif call.data == 'ref/item8':
        item_text = f'<b>{button_list["item8"]}</b>\n\n{button_list["item8_desc"]}\n\n' \
                     f'<b>Цена:</b> {button_list["item8_price"]} ₽\n\n' \
                     f'<b><a href="{button_list["item8_ref"]}">Ссылка на товар</a></b>'
        bot.send_photo(call.message.chat.id, open('media/images/perf/keyboard/item8.jpg', 'rb'),
                       parse_mode='html', caption=item_text)

    # HEADPHONES
    elif call.data == 'ref/item23':
        id_ = '23'
        item_text = f'<b>{button_list[f"item{id_}"]}</b>\n\n{button_list[f"item{id_}_desc"]}\n\n' \
                     f'<b>Цена:</b> {button_list[f"item{id_}_price"]} ₽\n\n' \
                     f'<b><a href="{button_list[f"item{id_}_ref"]}">Ссылка на товар</a></b>'
        bot.send_photo(call.message.chat.id, open(f'media/images/perf/headphones/item{id_}.jpg', 'rb'),
                       parse_mode='html', caption=item_text)
    elif call.data == 'ref/item24':
        id_ = '24'
        item_text = f'<b>{button_list[f"item{id_}"]}</b>\n\n{button_list[f"item{id_}_desc"]}\n\n' \
                     f'<b>Цена:</b> {button_list[f"item{id_}_price"]} ₽\n\n' \
                     f'<b><a href="{button_list[f"item{id_}_ref"]}">Ссылка на товар</a></b>'
        bot.send_photo(call.message.chat.id, open(f'media/images/perf/headphones/item{id_}.jpg', 'rb'),
                       parse_mode='html', caption=item_text)

    # COMP (MINING)
    if call.data == 'ref/item4':
        item_text = f'<b>{button_list["item4"]}</b>\n\n{button_list["item4_desc"]}\n\n' \
                     f'<b>Цена:</b> {button_list["item4_price"]} ₽\n\n' \
                     f'<b><a href="{button_list["item4_ref"]}">Ссылка на товар</a></b>'
        bot.send_photo(call.message.chat.id, open('media/images/comp/mining/item4.jpg', 'rb'),
                       parse_mode='html', caption=item_text)

    elif call.data == 'ref/item5':
        item_text = f'<b>{button_list["item5"]}</b>\n\n{button_list["item5_desc"]}\n\n' \
                     f'<b>Цена:</b> {button_list["item5_price"]} ₽\n\n' \
                     f'<b><a href="{button_list["item5_ref"]}">Ссылка на товар</a></b>'
        bot.send_photo(call.message.chat.id, open('media/images/comp/mining/item5.jpg', 'rb'),
                       parse_mode='html', caption=item_text)
    # COMP (PC)
    # PROCESSOR
    if call.data == 'ref/item9':
        id_ = '9'
        item_text = f'<b>{button_list[f"item{id_}"]}</b>\n\n{button_list[f"item{id_}_desc"]}\n\n' \
                     f'<b>Цена:</b> {button_list[f"item{id_}_price"]} ₽\n\n' \
                     f'<b><a href="{button_list[f"item{id_}_ref"]}">Ссылка на товар</a></b>'
        bot.send_photo(call.message.chat.id, open(f'media/images/comp/pc/processor/item{id_}.jpg', 'rb'),
                       parse_mode='html', caption=item_text)

    # VIDEOCARD
    elif call.data == 'ref/item10':
        id_ = '10'
        item_text = f'<b>{button_list[f"item{id_}"]}</b>\n\n{button_list[f"item{id_}_desc"]}\n\n' \
                     f'<b>Цена:</b> {button_list[f"item{id_}_price"]} ₽\n\n' \
                     f'<b><a href="{button_list[f"item{id_}_ref"]}">Ссылка на товар</a></b>'
        bot.send_photo(call.message.chat.id, open(f'media/images/comp/pc/videocard/item{id_}.jpg', 'rb'),
                       parse_mode='html', caption=item_text)
        bot.send_message(call.message.chat.id, f'Данный товар еще не был добавлен на площадку <b>Avito</b>.\n'
                                               f'За покупкой обращаться к <b>менеджеру: </b>@Septemshop_manager',
                         parse_mode='html')

    elif call.data == 'ref/item12':
        id_ = '12'
        item_text = f'<b>{button_list[f"item{id_}"]}</b>\n\n{button_list[f"item{id_}_desc"]}\n\n' \
                     f'<b>Цена:</b> {button_list[f"item{id_}_price"]} ₽\n\n' \
                     f'<b><a href="{button_list[f"item{id_}_ref"]}">Ссылка на товар</a></b>'
        bot.send_photo(call.message.chat.id, open(f'media/images/comp/pc/videocard/item{id_}.jpg', 'rb'),
                       parse_mode='html', caption=item_text)
        bot.send_message(call.message.chat.id, f'Данный товар еще не был добавлен на площадку <b>Avito</b>.\n'
                                               f'За покупкой обращаться к <b>менеджеру: </b>@Septemshop_manager',
                         parse_mode='html')

    elif call.data == 'ref/item14':
        id_ = '14'
        item_text = f'<b>{button_list[f"item{id_}"]}</b>\n\n{button_list[f"item{id_}_desc"]}\n\n' \
                     f'<b>Цена:</b> {button_list[f"item{id_}_price"]} ₽\n\n' \
                     f'<b><a href="{button_list[f"item{id_}_ref"]}">Ссылка на товар</a></b>'
        bot.send_photo(call.message.chat.id, open(f'media/images/comp/pc/videocard/item{id_}.jpg', 'rb'),
                       parse_mode='html', caption=item_text)
        bot.send_message(call.message.chat.id, f'Данный товар еще не был добавлен на площадку <b>Avito</b>.\n'
                                               f'За покупкой обращаться к <b>менеджеру: </b>@Septemshop_manager',
                         parse_mode='html')

    elif call.data == 'ref/item21':
        id_ = '21'
        item_text = f'<b>{button_list[f"item{id_}"]}</b>\n\n{button_list[f"item{id_}_desc"]}\n\n' \
                     f'<b>Цена:</b> {button_list[f"item{id_}_price"]} ₽\n\n' \
                     f'<b><a href="{button_list[f"item{id_}_ref"]}">Ссылка на товар</a></b>'
        bot.send_photo(call.message.chat.id, open(f'media/images/comp/pc/videocard/item{id_}.jpg', 'rb'),
                       parse_mode='html', caption=item_text)
        bot.send_message(call.message.chat.id, f'Данный товар еще не был добавлен на площадку <b>Avito</b>.\n'
                                               f'За покупкой обращаться к <b>менеджеру: </b>@Septemshop_manager',
                         parse_mode='html')

    elif call.data == 'ref/item22':
        id_ = '9'
        item_text = f'<b>{button_list[f"item{id_}"]}</b>\n\n{button_list[f"item{id_}_desc"]}\n\n' \
                     f'<b>Цена:</b> {button_list[f"item{id_}_price"]} ₽\n\n' \
                     f'<b><a href="{button_list[f"item{id_}_ref"]}">Ссылка на товар</a></b>'
        bot.send_photo(call.message.chat.id, open(f'media/images/comp/pc/videocard/item{id_}.jpg', 'rb'),
                       parse_mode='html', caption=item_text)
        bot.send_message(call.message.chat.id, f'Данный товар еще не был добавлен на площадку <b>Avito</b>.\n'
                                               f'За покупкой обращаться к <b>менеджеру: </b>@Septemshop_manager',
                         parse_mode='html')

    # MOTHERBOARD
    elif call.data == 'ref/item11':
        id_ = '11'
        item_text = f'<b>{button_list[f"item{id_}"]}</b>\n\n{button_list[f"item{id_}_desc"]}\n\n' \
                     f'<b>Цена:</b> {button_list[f"item{id_}_price"]} ₽\n\n' \
                     f'<b><a href="{button_list[f"item{id_}_ref"]}">Ссылка на товар</a></b>'
        bot.send_photo(call.message.chat.id, open(f'media/images/comp/pc/motherboard/item{id_}.jpg', 'rb'),
                       parse_mode='html', caption=item_text)
        bot.send_message(call.message.chat.id, f'Данный товар еще не был добавлен на площадку <b>Avito</b>.\n'
                                               f'За покупкой обращаться к <b>менеджеру: </b>@Septemshop_manager',
                         parse_mode='html')

    elif call.data == 'ref/item15':
        id_ = '15'
        item_text = f'<b>{button_list[f"item{id_}"]}</b>\n\n{button_list[f"item{id_}_desc"]}\n\n' \
                    f'<b>Цена:</b> {button_list[f"item{id_}_price"]} ₽\n\n' \
                    f'<b><a href="{button_list[f"item{id_}_ref"]}">Ссылка на товар</a></b>'
        bot.send_photo(call.message.chat.id, open(f'media/images/comp/pc/motherboard/item{id_}.jpg', 'rb'),
                       parse_mode='html', caption=item_text)
        bot.send_message(call.message.chat.id, f'Данный товар еще не был добавлен на площадку <b>Avito</b>.\n'
                                               f'За покупкой обращаться к <b>менеджеру: </b>@Septemshop_manager',
                         parse_mode='html')

    elif call.data == 'ref/item16':
        id_ = '16'
        item_text = f'<b>{button_list[f"item{id_}"]}</b>\n\n{button_list[f"item{id_}_desc"]}\n\n' \
                    f'<b>Цена:</b> {button_list[f"item{id_}_price"]} ₽\n\n' \
                    f'<b><a href="{button_list[f"item{id_}_ref"]}">Ссылка на товар</a></b>'
        bot.send_photo(call.message.chat.id, open(f'media/images/comp/pc/motherboard/item{id_}.jpg', 'rb'),
                       parse_mode='html', caption=item_text)
        bot.send_message(call.message.chat.id, f'Данный товар еще не был добавлен на площадку <b>Avito</b>.\n'
                                               f'За покупкой обращаться к <b>менеджеру: </b>@Septemshop_manager',
                         parse_mode='html')

    elif call.data == 'ref/item17':
        id_ = '17'
        item_text = f'<b>{button_list[f"item{id_}"]}</b>\n\n{button_list[f"item{id_}_desc"]}\n\n' \
                    f'<b>Цена:</b> {button_list[f"item{id_}_price"]} ₽\n\n' \
                    f'<b><a href="{button_list[f"item{id_}_ref"]}">Ссылка на товар</a></b>'
        bot.send_photo(call.message.chat.id, open(f'media/images/comp/pc/motherboard/item{id_}.jpg', 'rb'),
                       parse_mode='html', caption=item_text)
        bot.send_message(call.message.chat.id, f'Данный товар еще не был добавлен на площадку <b>Avito</b>.\n'
                                               f'За покупкой обращаться к <b>менеджеру: </b>@Septemshop_manager',
                         parse_mode='html')

    elif call.data == 'ref/item18':
        id_ = '18'
        item_text = f'<b>{button_list[f"item{id_}"]}</b>\n\n{button_list[f"item{id_}_desc"]}\n\n' \
                    f'<b>Цена:</b> {button_list[f"item{id_}_price"]} ₽\n\n' \
                    f'<b><a href="{button_list[f"item{id_}_ref"]}">Ссылка на товар</a></b>'
        bot.send_photo(call.message.chat.id, open(f'media/images/comp/pc/motherboard/item{id_}.jpg', 'rb'),
                       parse_mode='html', caption=item_text)
        bot.send_message(call.message.chat.id, f'Данный товар еще не был добавлен на площадку <b>Avito</b>.\n'
                                               f'За покупкой обращаться к <b>менеджеру: </b>@Septemshop_manager',
                         parse_mode='html')

    elif call.data == 'ref/item19':
        id_ = '19'
        item_text = f'<b>{button_list[f"item{id_}"]}</b>\n\n{button_list[f"item{id_}_desc"]}\n\n' \
                    f'<b>Цена:</b> {button_list[f"item{id_}_price"]} ₽\n\n' \
                    f'<b><a href="{button_list[f"item{id_}_ref"]}">Ссылка на товар</a></b>'
        bot.send_photo(call.message.chat.id, open(f'media/images/comp/pc/motherboard/item{id_}.jpg', 'rb'),
                       parse_mode='html', caption=item_text)
        bot.send_message(call.message.chat.id, f'Данный товар еще не был добавлен на площадку <b>Avito</b>.\n'
                                               f'За покупкой обращаться к <b>менеджеру: </b>@Septemshop_manager',
                         parse_mode='html')

    elif call.data == 'ref/item20':
        id_ = '20'
        item_text = f'<b>{button_list[f"item{id_}"]}</b>\n\n{button_list[f"item{id_}_desc"]}\n\n' \
                    f'<b>Цена:</b> {button_list[f"item{id_}_price"]} ₽\n\n' \
                    f'<b><a href="{button_list[f"item{id_}_ref"]}">Ссылка на товар</a></b>'
        bot.send_photo(call.message.chat.id, open(f'media/images/comp/pc/motherboard/item{id_}.jpg', 'rb'),
                       parse_mode='html', caption=item_text)
        bot.send_message(call.message.chat.id, f'Данный товар еще не был добавлен на площадку <b>Avito</b>.\n'
                                               f'За покупкой обращаться к <b>менеджеру: </b>@Septemshop_manager',
                         parse_mode='html')

    # GAME DEVICE
    if call.data == 'ref/item6':
        item_text = f'<b>{button_list["item6"]}</b>\n\n{button_list["item6_desc"]}\n\n' \
                     f'<b>Цена:</b> {button_list["item6_price"]} ₽\n\n' \
                     f'<b><a href="{button_list["item6_ref"]}">Ссылка на товар</a></b>'
        bot.send_photo(call.message.chat.id, open('media/images/gaming_devices/gamepad/item6.jpg', 'rb'),
                       parse_mode='html', caption=item_text)

    # FURN
    if call.data == 'ref/item7':
        item_text = f'<b>{button_list["item7"]}</b>\n\n{button_list["item7_desc"]}\n\n' \
                     f'<b>Цена:</b> {button_list["item7_price"]} ₽\n\n' \
                     f'<b><a href="{button_list["item7_ref"]}">Ссылка на товар</a></b>'
        bot.send_photo(call.message.chat.id, open('media/images/furn/chair/item7.jpg', 'rb'),
                       parse_mode='html', caption=item_text)

    bot.answer_callback_query(callback_query_id=call.id)


if __name__ == '__main__':
    bot.polling(none_stop=True)
