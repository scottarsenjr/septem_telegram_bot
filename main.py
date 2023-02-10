import telebot, sqlite3
from telebot import types
from config.id import button_list, faq_text, contact_info, search_text, item_name, item_desc, item_price, item_ref
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
            bot.send_message(message.chat.id, search_text, reply_markup=markup, parse_mode='html')

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
        item1 = types.InlineKeyboardButton(text=item_name['item1'], callback_data='ref/item1')
        item2 = types.InlineKeyboardButton(text=item_name['item2'], callback_data='ref/item2')
        main.add(item1, item2)
        bot.send_message(message.chat.id, 'Выберите товар из списка', reply_markup=main)

    elif message.text == button_list['keyboard']:
        main = types.InlineKeyboardMarkup(row_width=1)
        item3 = types.InlineKeyboardButton(text=item_name['item3'], callback_data='ref/item3')
        item8 = types.InlineKeyboardButton(text=item_name['item8'], callback_data='ref/item8')
        main.add(item3, item8)
        bot.send_message(message.chat.id, 'Выберите товар из списка', reply_markup=main)

    elif message.text == button_list['headphones']:
        main = types.InlineKeyboardMarkup(row_width=1)
        item23 = types.InlineKeyboardButton(text=item_name['item23'], callback_data='ref/item23')
        item24 = types.InlineKeyboardButton(text=item_name['item24'], callback_data='ref/item24')
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
        item9 = types.InlineKeyboardButton(text=item_name['item9'], callback_data='ref/item9')
        main.add(item9)
        bot.send_message(message.chat.id, 'Выберите товар из списка', reply_markup=main)

    elif message.text == button_list['videocard']:
        main = types.InlineKeyboardMarkup(row_width=1)
        item10 = types.InlineKeyboardButton(text=item_name['item10'], callback_data='ref/item10')
        item12 = types.InlineKeyboardButton(text=item_name['item12'], callback_data='ref/item12')
        item14 = types.InlineKeyboardButton(text=item_name['item14'], callback_data='ref/item14')
        item21 = types.InlineKeyboardButton(text=item_name['item21'], callback_data='ref/item21')
        item22 = types.InlineKeyboardButton(text=item_name['item22'], callback_data='ref/item22')
        main.add(item10, item12, item14, item21, item22)
        bot.send_message(message.chat.id, 'Выберите товар из списка', reply_markup=main)

    elif message.text == button_list['motherboard']:
        main = types.InlineKeyboardMarkup(row_width=1)
        item11 = types.InlineKeyboardButton(text=item_name['item11'], callback_data='ref/item11')
        item15 = types.InlineKeyboardButton(text=item_name['item15'], callback_data='ref/item15')
        item16 = types.InlineKeyboardButton(text=item_name['item16'], callback_data='ref/item16')
        item17 = types.InlineKeyboardButton(text=item_name['item17'], callback_data='ref/item17')
        item18 = types.InlineKeyboardButton(text=item_name['item18'], callback_data='ref/item18')
        item19 = types.InlineKeyboardButton(text=item_name['item19'], callback_data='ref/item19')
        item20 = types.InlineKeyboardButton(text=item_name['item20'], callback_data='ref/item20')
        main.add(item11, item15, item16, item17, item18, item19, item20)
        bot.send_message(message.chat.id, 'Выберите товар из списка', reply_markup=main)

    # MINING SUB-MENU (COMP)
    if message.text == button_list['motherboard_mining']:
        main = types.InlineKeyboardMarkup(row_width=1)
        item4 = types.InlineKeyboardButton(text=item_name['item4'], callback_data='ref/item4')
        main.add(item4)
        bot.send_message(message.chat.id, 'Выберите товар из списка', reply_markup=main)

    elif message.text == button_list['case_mining']:
        main = types.InlineKeyboardMarkup(row_width=1)
        item5 = types.InlineKeyboardButton(text=item_name['item5'], callback_data='ref/item5')
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
        item6 = types.InlineKeyboardButton(text=item_name['item6'], callback_data='ref/item6')
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
        item7 = types.InlineKeyboardButton(text=item_name['item7'], callback_data='ref/item7')
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


def request(message):
    request = message.text
    bot.send_message(message.chat.id, request)


@bot.callback_query_handler(func=lambda call: True)
def refs(call):
    products = 25
    for i in range(1, products):
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
