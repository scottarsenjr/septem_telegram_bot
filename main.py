import telebot, sqlite3
from telebot import types
from config.id import button_list, faq_text,\
    contact_info, search_text, item_name, item_desc, item_price, item_ref, amount, product_list
from config.token import bot


@bot.message_handler(commands=['start'])
def start(message):
    # Menu Appear
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    products = types.KeyboardButton(button_list['products'])
    search = types.KeyboardButton(button_list['search'])
    faq = types.KeyboardButton(button_list['faq'])
    contacts = types.KeyboardButton(button_list['contacts'])

    markup.add(products, search, faq, contacts)

    # Greeting
    greet = f'Добро пожаловать в <b>Septem Shop</b> 🔥 <u>{message.from_user.first_name}</u>!\n'
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_animation(message.chat.id, open('media/gif/septemshopgif.gif', 'rb'), caption=greet,
                       parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'], func=lambda message: True)
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

        elif message.text == button_list['search']:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            return_ = types.KeyboardButton(button_list['return'])
            markup.add(return_)
            send = bot.send_message(message.chat.id, search_text, parse_mode='html', reply_markup=markup)
            bot.register_next_step_handler(send, search_func)

        elif message.text == button_list['faq']:
            bot.send_message(message.chat.id, faq_text, parse_mode='MarkdownV2', disable_web_page_preview=True)

        elif message.text == button_list['contacts']:
            bot.send_message(message.chat.id, contact_info, parse_mode='html')

        # BACK TO MENU
        elif message.text == button_list['return']:
            bot.send_message(message.chat.id, 'Пожалуйста, подождите.')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            products = types.KeyboardButton(button_list['products'])
            search = types.KeyboardButton(button_list['search'])
            faq = types.KeyboardButton(button_list['faq'])
            contacts = types.KeyboardButton(button_list['contacts'])

            markup.add(products, search, faq, contacts)

            greet = f'Добро пожаловать в <b>Septem Shop</b> 🔥 <u>{message.from_user.first_name}</u>!\n'
            bot.send_chat_action(message.chat.id, 'typing')
            bot.send_animation(message.chat.id, open('media/gif/septemshopgif.gif', 'rb'), caption=greet,
                               parse_mode='html', reply_markup=markup)

        elif message.text == button_list['main_menu']:
            bot.send_message(message.chat.id, 'Пожалуйста подождите.')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            products = types.KeyboardButton(button_list['products'])
            search = types.KeyboardButton(button_list['search'])
            faq = types.KeyboardButton(button_list['faq'])
            contacts = types.KeyboardButton(button_list['contacts'])

            markup.add(products, search, faq, contacts)

            greet = f'Добро пожаловать в <b>Septem Shop</b> 🔥 <u>{message.from_user.first_name}</u>!\n'
            bot.send_chat_action(message.chat.id, 'typing')
            bot.send_animation(message.chat.id, open('media/gif/septemshopgif.gif', 'rb'), caption=greet,
                               parse_mode='html', reply_markup=markup)

    # PERF MENU
    if message.text == button_list['perf']:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        monitor = types.KeyboardButton(button_list['monitor'])
        mouse = types.KeyboardButton(button_list['mouse'])
        keyboard = types.KeyboardButton(button_list['keyboard'])
        headphones = types.KeyboardButton(button_list['headphones'])
        back = types.KeyboardButton(button_list['back_product'])

        markup.add(monitor, keyboard, headphones, mouse, back)
        bot.send_message(message.chat.id, 'Выберите подкатегорию для категории "Периферия"',
                         parse_mode='html', reply_markup=markup)

    # PERF SUB-MENU
    if message.text == button_list['monitor']:
        main = types.InlineKeyboardMarkup(row_width=1)
        connect = sqlite3.connect('database/products.db')
        cursor = connect.cursor()
        listed = []
        for request, in cursor.execute('SELECT id FROM Products WHERE sub_category="Монитор"'):
            listed.append(request)
        connect.commit()
        for i in range(len(listed)):
            id_ = str(listed[i])
            item_inline = types.InlineKeyboardButton(text=item_name[f'item{id_}'], callback_data=f'ref/item{id_}')
            main.add(item_inline)
        bot.send_message(message.chat.id, 'Выберите товар из списка', reply_markup=main)

    elif message.text == button_list['keyboard']:
        main = types.InlineKeyboardMarkup(row_width=1)
        connect = sqlite3.connect('database/products.db')
        cursor = connect.cursor()
        listed = []
        for request, in cursor.execute('SELECT id FROM Products WHERE sub_category="Клавиатура"'):
            listed.append(request)
        connect.commit()
        for i in range(len(listed)):
            id_ = str(listed[i])
            item_inline = types.InlineKeyboardButton(text=item_name[f'item{id_}'], callback_data=f'ref/item{id_}')
            main.add(item_inline)
        bot.send_message(message.chat.id, 'Выберите товар из списка', reply_markup=main)

    elif message.text == button_list['headphones']:
        main = types.InlineKeyboardMarkup(row_width=1)
        connect = sqlite3.connect('database/products.db')
        cursor = connect.cursor()
        listed = []
        for request, in cursor.execute('SELECT id FROM Products WHERE sub_category="Наушники"'):
            listed.append(request)
        connect.commit()
        for i in range(len(listed)):
            id_ = str(listed[i])
            item_inline = types.InlineKeyboardButton(text=item_name[f'item{id_}'], callback_data=f'ref/item{id_}')
            main.add(item_inline)
        bot.send_message(message.chat.id, 'Выберите товар из списка', reply_markup=main)

    elif message.text == button_list['mouse']:
        main = types.InlineKeyboardMarkup(row_width=1)
        connect = sqlite3.connect('database/products.db')
        cursor = connect.cursor()
        listed = []
        for request, in cursor.execute('SELECT id FROM Products WHERE sub_category="Компьютерная мышь"'):
            listed.append(request)
        connect.commit()
        for i in range(len(listed)):
            id_ = str(listed[i])
            item_inline = types.InlineKeyboardButton(text=item_name[f'item{id_}'], callback_data=f'ref/item{id_}')
            main.add(item_inline)
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
        videocard = types.KeyboardButton(button_list['videocard_mining'])
        back = types.KeyboardButton(button_list['back_product_comp'])
        markup.add(motherboard, case, videocard, back)

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
        connect = sqlite3.connect('database/products.db')
        cursor = connect.cursor()
        listed = []
        for request, in cursor.execute('SELECT id FROM Products WHERE sub_category="Процессор"'):
            listed.append(request)
        connect.commit()
        for i in range(len(listed)):
            id_ = str(listed[i])
            item_inline = types.InlineKeyboardButton(text=item_name[f'item{id_}'], callback_data=f'ref/item{id_}')
            main.add(item_inline)
        bot.send_message(message.chat.id, 'Выберите товар из списка', reply_markup=main)

    elif message.text == button_list['videocard']:
        main = types.InlineKeyboardMarkup(row_width=1)
        connect = sqlite3.connect('database/products.db')
        cursor = connect.cursor()
        listed = []
        for request, in cursor.execute('SELECT id FROM Products WHERE sub_category="Видеокарта"'):
            listed.append(request)
        connect.commit()
        for i in range(len(listed)):
            id_ = str(listed[i])
            item_inline = types.InlineKeyboardButton(text=item_name[f'item{id_}'], callback_data=f'ref/item{id_}')
            main.add(item_inline)
        bot.send_message(message.chat.id, 'Выберите товар из списка', reply_markup=main)

    elif message.text == button_list['motherboard']:
        main = types.InlineKeyboardMarkup(row_width=1)
        connect = sqlite3.connect('database/products.db')
        cursor = connect.cursor()
        listed = []
        for request, in cursor.execute('SELECT id FROM Products WHERE sub_category="Материнская плата"'):
            listed.append(request)
        connect.commit()
        for i in range(len(listed)):
            id_ = str(listed[i])
            item_inline = types.InlineKeyboardButton(text=item_name[f'item{id_}'], callback_data=f'ref/item{id_}')
            main.add(item_inline)
        bot.send_message(message.chat.id, 'Выберите товар из списка', reply_markup=main)

    # MINING SUB-MENU (COMP)
    if message.text == button_list['motherboard_mining']:
        main = types.InlineKeyboardMarkup(row_width=1)
        connect = sqlite3.connect('database/products.db')
        cursor = connect.cursor()
        listed = []
        for request, in cursor.execute('SELECT id FROM Products WHERE sub_category="Материнская плата майнинг"'):
            listed.append(request)
        connect.commit()
        for i in range(len(listed)):
            id_ = str(listed[i])
            item_inline = types.InlineKeyboardButton(text=item_name[f'item{id_}'], callback_data=f'ref/item{id_}')
            main.add(item_inline)
        bot.send_message(message.chat.id, 'Выберите товар из списка', reply_markup=main)

    elif message.text == button_list['case_mining']:
        main = types.InlineKeyboardMarkup(row_width=1)
        connect = sqlite3.connect('database/products.db')
        cursor = connect.cursor()
        listed = []
        for request, in cursor.execute('SELECT id FROM Products WHERE sub_category="Корпус майнинг"'):
            listed.append(request)
        connect.commit()
        for i in range(len(listed)):
            id_ = str(listed[i])
            item_inline = types.InlineKeyboardButton(text=item_name[f'item{id_}'], callback_data=f'ref/item{id_}')
            main.add(item_inline)
        bot.send_message(message.chat.id, 'Выберите товар из списка', reply_markup=main)

    elif message.text == button_list['videocard_mining']:
        main = types.InlineKeyboardMarkup(row_width=1)
        connect = sqlite3.connect('database/products.db')
        cursor = connect.cursor()
        listed = []
        for request, in cursor.execute('SELECT id FROM Products WHERE sub_category="Видеокарта майнинг"'):
            listed.append(request)
        connect.commit()
        for i in range(len(listed)):
            id_ = str(listed[i])
            item_inline = types.InlineKeyboardButton(text=item_name[f'item{id_}'], callback_data=f'ref/item{id_}')
            main.add(item_inline)
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
        connect = sqlite3.connect('database/products.db')
        cursor = connect.cursor()
        listed = []
        for request, in cursor.execute('SELECT id FROM Products WHERE sub_category="Геймпады"'):
            listed.append(request)
        connect.commit()
        for i in range(len(listed)):
            id_ = str(listed[i])
            item_inline = types.InlineKeyboardButton(text=item_name[f'item{id_}'], callback_data=f'ref/item{id_}')
            main.add(item_inline)
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
        connect = sqlite3.connect('database/products.db')
        cursor = connect.cursor()
        listed = []
        for request, in cursor.execute('SELECT id FROM Products WHERE sub_category="Кресла"'):
            listed.append(request)
        connect.commit()
        for i in range(len(listed)):
            id_ = str(listed[i])
            item_inline = types.InlineKeyboardButton(text=item_name[f'item{id_}'], callback_data=f'ref/item{id_}')
            main.add(item_inline)
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


def lower_func(s):
    return s.lower()


def search_func(message):
    if message.text == button_list['return']:
        bot.send_message(message.chat.id, 'Пожалуйста, подождите.')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        products = types.KeyboardButton(button_list['products'])
        search = types.KeyboardButton(button_list['search'])
        faq = types.KeyboardButton(button_list['faq'])
        contacts = types.KeyboardButton(button_list['contacts'])

        markup.add(products, search, faq, contacts)

        greet = f'Добро пожаловать в <b>Septem Shop</b> 🔥 <u>{message.from_user.first_name}</u>!\n'
        bot.send_chat_action(message.chat.id, 'typing')
        bot.send_animation(message.chat.id, open('media/gif/septemshopgif.gif', 'rb'), caption=greet,
                           parse_mode='html', reply_markup=markup)
    else:
        while message.text != button_list['return']:
            if (message.text[0:2].lower() == 'ID'.lower()) and message.text[2:].isdigit() and (1 <= int(message.text[2:]) < amount):
                id_ = int(message.text[2:])
                item_text = f'<b>{item_name[f"item{id_}"]}</b>\n\n{item_desc[f"item{id_}_desc"]}\n\n' \
                            f'<b>Цена:</b> {item_price[f"item{id_}_price"]} ₽\n\n' \
                            f'<b><a href="{item_ref[f"item{id_}_ref"]}">Ссылка на товар</a></b>'
                if item_ref[f"item{id_}_ref"] != '':
                    send = bot.send_photo(message.chat.id, open(f'media/images/item{id_}.jpg', 'rb'),
                                          parse_mode='html', caption=item_text)
                    bot.register_next_step_handler(send, search_func)
                    break
                else:
                    send = bot.send_photo(message.chat.id, open(f'media/images/item{id_}.jpg', 'rb'),
                                          parse_mode='html', caption=item_text)
                    bot.send_message(message.chat.id,
                                     f'Данный товар еще не был добавлен на площадку <b>Avito</b>.\n'
                                     f'За покупкой обращаться к <b>менеджеру: </b>@Septemshop_manager',
                                     parse_mode='html')
                    bot.register_next_step_handler(send, search_func)
                    break
            else:
                connect = sqlite3.connect('database/products.db')
                connect.create_function('lower_func', 1, lower_func)
                cursor = connect.cursor()
                listed = []
                for request, in cursor.execute('SELECT name FROM Products WHERE lower_func(name) LIKE lower(?)', [f'%{message.text.lower()}%']):
                    listed.append(request)
                connect.commit()
                if len(listed) == 0:
                    fail = bot.send_message(message.chat.id, 'Указанный товар не найден.')
                    bot.register_next_step_handler(fail, search_func)
                    break
                else:
                    main = types.InlineKeyboardMarkup(row_width=1)
                    for i in range(len(listed)):
                        id_ = str(*cursor.execute(f'SELECT id FROM Products WHERE name="{listed[i]}"').fetchone())
                        item_inline = types.InlineKeyboardButton(text=item_name[f'item{id_}'], callback_data=f'ref/item{id_}')
                        main.add(item_inline)
                    listed.clear()
                    send = bot.send_message(message.chat.id, f'Товары найденные по запросу "{message.text}"', reply_markup=main)
                    bot.register_next_step_handler(send, search_func)
                    break


@bot.callback_query_handler(func=lambda call: True)
def refs(call):
    for i in range(1, amount):
        if call.data == f'ref/item{str(i)}':
            id_ = str(i)
            item_text = f'<b>{item_name[f"item{id_}"]}</b>\n\n{item_desc[f"item{id_}_desc"]}\n\n' \
                         f'<b>Цена:</b> {item_price[f"item{id_}_price"]} ₽\n\n' \
                         f'<b><a href="{item_ref[f"item{id_}_ref"]}">Ссылка на товар</a></b>'
            if item_ref[f"item{id_}_ref"] != '':
                bot.send_photo(call.message.chat.id, open(f'media/images/item{id_}.jpg', 'rb'),
                               parse_mode='html', caption=item_text)
            else:
                bot.send_photo(call.message.chat.id, open(f'media/images/item{id_}.jpg', 'rb'),
                               parse_mode='html', caption=item_text)
                bot.send_message(call.message.chat.id, f'Данный товар еще не был добавлен на площадку <b>Avito</b>.\n'
                                                       f'За покупкой обращаться к <b>менеджеру: </b>@Septemshop_manager',
                                 parse_mode='html')

    bot.answer_callback_query(callback_query_id=call.id)


if __name__ == '__main__':
    bot.polling(none_stop=True)
