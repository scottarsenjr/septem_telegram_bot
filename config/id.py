import sqlite3

# URLS
shop = 'https://www.avito.ru/user/fe04ff3c91b5db23fdbdd34e83d3be05/profile?id=2779976873&src=item&page_from=from_item_card&iid=2779976873/'

search_text = f"""
<b>🔎 Поиск товара по названию или ID</b>

Чтобы найти необходимый вам товар, отправьте боту сообщение в виде индивидуального
идентификатора <b>ID</b> или <b>названия</b>.

<b><u>Пример</u></b>:
"ID<b>3</b>" => "Клавиатура HyperX Alloy Origins Core TKL механическая черный USB for gamer LED"

"Монитор Acer" => "Монитор 23,8" acer Nitro QG241YPbmiipx 165hz"
"""

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

contact_info = """
<b>Контактная информация</b>

По всем вопросам обращаться к администраторам

@Septemshop_manager либо @septemshop_tech
            """

# DB CONNECT
connect = sqlite3.connect('database/products.db')
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Products(
    id INTEGER,
    category TEXT,
    sub_category TEXT,
    name TEXT,
    description TEXT,
    ref TEXT,
    price INTEGER
)""")

button_list = {
    # MAIN MENU
    'products': '🛒 Товары',
    'search': '🔎 Найти товар',
    'faq': '🤔 Часто задаваемые вопросы',
    'contacts': '☎️ Контакты',

    # SEARCH
    'return': '↵ Вернуться в главное меню',

    # BACK BUTTONS
    'main_menu': '↵ В главное меню',
    'back_product': '↵ Вернуться к категориям',
    'back_product_comp': '↵ Вернуться к подкатегориям',

    # CATEGORIES
    'perf': '🖥️ Периферия и аксессуары',
    'comp': '💽 Комплектующие',
    'furn': '💺 Офисное оборудование и мебель',
    'game_device': '🕹️ Игровые устройства',

    # SUB CATEGORIES (PERF)
    'monitor': '🖥️ Мониторы',
    'mouse': '🖱️ Компьютерные мыши',
    'keyboard': '⌨️ Компьютерные клавиатуры',
    'headphones': '🎧 Наушники',

    # SUB CATEGORIES (COMP)
    'pc': '💽 Комплектующие для ПК',
    'mining': '💰 Комплектующие для майнинга',

    # SUB CATEGORIES (COMP MINING)
    'motherboard_mining': '✳️ Материнские платы',
    'case_mining': '🧰 Корпусы',

    # SUB CATEGORIES (COMP PC)
    'motherboard': '🟨 Материнские платы',
    'processor': '🟢 Процессоры',
    'videocard': '🎞️ Видеокарты',

    # SUB CATEGORIES (GAME DEVICES)
    'gamepad': '🎮 Геймпады',

    # SUB CATEGORIES (FURN)
    'chair': '🪑 Кресла',
}

connect.commit()

item_name = {}
product_list = []
amount = 28
for i in range(1, amount):
    values = [f'item{str(i)}', str(*cursor.execute(f'SELECT name FROM Products WHERE id = {i}').fetchone())]
    product_list.append(str(*cursor.execute(f'SELECT name FROM Products WHERE id = {i}').fetchone()))
    item_name.update([values])


item_desc = {}
for i in range(1, amount):
    values = [f'item{str(i)}_desc',  str(*cursor.execute(f'SELECT description FROM Products WHERE id = {i}').fetchone())]
    item_desc.update([values])


item_price = {}
for i in range(1, amount):
    values = [f'item{str(i)}_price', str(*cursor.execute(f'SELECT price FROM Products WHERE id = {i}').fetchone())]
    item_price.update([values])


item_ref = {}
for i in range(1, amount):
    values = [f'item{str(i)}_ref', str(*cursor.execute(f'SELECT ref FROM Products WHERE id = {i}').fetchone())]
    item_ref.update([values])
