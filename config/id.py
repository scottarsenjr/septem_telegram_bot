import sqlite3

# URLS
shop = 'https://www.avito.ru/user/fe04ff3c91b5db23fdbdd34e83d3be05/profile?id=2779976873&src=item&page_from=from_item_card&iid=2779976873/'

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
    'faq': '🤔 Часто задаваемые вопросы',
    'contacts': '☎️ Контакты',

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

    # PERF
    'item1': str(*cursor.execute('SELECT name FROM Products WHERE id = 1').fetchone()),
    'item1_desc': str(*cursor.execute('SELECT description FROM Products WHERE id = 1').fetchone()),
    'item1_price': str(*cursor.execute('SELECT price FROM Products WHERE id = 1').fetchone()),
    'item1_ref': str(*cursor.execute('SELECT ref FROM Products WHERE id = 1').fetchone()),

    'item2': str(*cursor.execute('SELECT name FROM Products WHERE id = 2').fetchone()),
    'item2_desc': str(*cursor.execute('SELECT description FROM Products WHERE id = 2').fetchone()),
    'item2_price': str(*cursor.execute('SELECT price FROM Products WHERE id = 2').fetchone()),
    'item2_ref': str(*cursor.execute('SELECT ref FROM Products WHERE id = 2').fetchone()),

    'item3': str(*cursor.execute('SELECT name FROM Products WHERE id = 3').fetchone()),
    'item3_desc': str(*cursor.execute('SELECT description FROM Products WHERE id = 3').fetchone()),
    'item3_price': str(*cursor.execute('SELECT price FROM Products WHERE id = 3').fetchone()),
    'item3_ref': str(*cursor.execute('SELECT ref FROM Products WHERE id = 3').fetchone()),

    'item23': str(*cursor.execute('SELECT name FROM Products WHERE id = 23').fetchone()),
    'item23_desc': str(*cursor.execute('SELECT description FROM Products WHERE id = 23').fetchone()),
    'item23_price': str(*cursor.execute('SELECT price FROM Products WHERE id = 23').fetchone()),
    'item23_ref': str(*cursor.execute('SELECT ref FROM Products WHERE id = 23').fetchone()),

    'item24': str(*cursor.execute('SELECT name FROM Products WHERE id = 24').fetchone()),
    'item24_desc': str(*cursor.execute('SELECT description FROM Products WHERE id = 24').fetchone()),
    'item24_price': str(*cursor.execute('SELECT price FROM Products WHERE id = 24').fetchone()),
    'item24_ref': str(*cursor.execute('SELECT ref FROM Products WHERE id = 24').fetchone()),

    # COMP MINING
    'item4': str(*cursor.execute('SELECT name FROM Products WHERE id = 4').fetchone()),
    'item4_desc': str(*cursor.execute('SELECT description FROM Products WHERE id = 4').fetchone()),
    'item4_price': str(*cursor.execute('SELECT price FROM Products WHERE id = 4').fetchone()),
    'item4_ref': str(*cursor.execute('SELECT ref FROM Products WHERE id = 4').fetchone()),

    'item5': str(*cursor.execute('SELECT name FROM Products WHERE id = 5').fetchone()),
    'item5_desc': str(*cursor.execute('SELECT description FROM Products WHERE id = 5').fetchone()),
    'item5_price': str(*cursor.execute('SELECT price FROM Products WHERE id = 5').fetchone()),
    'item5_ref': str(*cursor.execute('SELECT ref FROM Products WHERE id = 5').fetchone()),

    # COMP PC
    'item9': str(*cursor.execute('SELECT name FROM Products WHERE id = 9').fetchone()),
    'item9_desc': str(*cursor.execute('SELECT description FROM Products WHERE id = 9').fetchone()),
    'item9_price': str(*cursor.execute('SELECT price FROM Products WHERE id = 9').fetchone()),
    'item9_ref': str(*cursor.execute('SELECT ref FROM Products WHERE id = 9').fetchone()),

    'item10': str(*cursor.execute('SELECT name FROM Products WHERE id = 10').fetchone()),
    'item10_desc': str(*cursor.execute('SELECT description FROM Products WHERE id = 10').fetchone()),
    'item10_price': str(*cursor.execute('SELECT price FROM Products WHERE id = 10').fetchone()),
    'item10_ref': str(*cursor.execute('SELECT ref FROM Products WHERE id = 10').fetchone()),

    'item11': str(*cursor.execute('SELECT name FROM Products WHERE id = 11').fetchone()),
    'item11_desc': str(*cursor.execute('SELECT description FROM Products WHERE id = 11').fetchone()),
    'item11_price': str(*cursor.execute('SELECT price FROM Products WHERE id = 11').fetchone()),
    'item11_ref': str(*cursor.execute('SELECT ref FROM Products WHERE id = 11').fetchone()),

    'item12': str(*cursor.execute('SELECT name FROM Products WHERE id = 12').fetchone()),
    'item12_desc': str(*cursor.execute('SELECT description FROM Products WHERE id = 12').fetchone()),
    'item12_price': str(*cursor.execute('SELECT price FROM Products WHERE id = 12').fetchone()),
    'item12_ref': str(*cursor.execute('SELECT ref FROM Products WHERE id = 12').fetchone()),

    'item13': str(*cursor.execute('SELECT name FROM Products WHERE id = 13').fetchone()),
    'item13_desc': str(*cursor.execute('SELECT description FROM Products WHERE id = 13').fetchone()),
    'item13_price': str(*cursor.execute('SELECT price FROM Products WHERE id = 13').fetchone()),
    'item13_ref': str(*cursor.execute('SELECT ref FROM Products WHERE id = 13').fetchone()),

    'item14': str(*cursor.execute('SELECT name FROM Products WHERE id = 14').fetchone()),
    'item14_desc': str(*cursor.execute('SELECT description FROM Products WHERE id = 14').fetchone()),
    'item14_price': str(*cursor.execute('SELECT price FROM Products WHERE id = 14').fetchone()),
    'item14_ref': str(*cursor.execute('SELECT ref FROM Products WHERE id = 14').fetchone()),

    'item15': str(*cursor.execute('SELECT name FROM Products WHERE id = 15').fetchone()),
    'item15_desc': str(*cursor.execute('SELECT description FROM Products WHERE id = 15').fetchone()),
    'item15_price': str(*cursor.execute('SELECT price FROM Products WHERE id = 15').fetchone()),
    'item15_ref': str(*cursor.execute('SELECT ref FROM Products WHERE id = 15').fetchone()),

    'item16': str(*cursor.execute('SELECT name FROM Products WHERE id = 16').fetchone()),
    'item16_desc': str(*cursor.execute('SELECT description FROM Products WHERE id = 16').fetchone()),
    'item16_price': str(*cursor.execute('SELECT price FROM Products WHERE id = 16').fetchone()),
    'item16_ref': str(*cursor.execute('SELECT ref FROM Products WHERE id = 16').fetchone()),

    'item17': str(*cursor.execute('SELECT name FROM Products WHERE id = 17').fetchone()),
    'item17_desc': str(*cursor.execute('SELECT description FROM Products WHERE id = 17').fetchone()),
    'item17_price': str(*cursor.execute('SELECT price FROM Products WHERE id = 17').fetchone()),
    'item17_ref': str(*cursor.execute('SELECT ref FROM Products WHERE id = 17').fetchone()),

    'item18': str(*cursor.execute('SELECT name FROM Products WHERE id = 18').fetchone()),
    'item18_desc': str(*cursor.execute('SELECT description FROM Products WHERE id = 18').fetchone()),
    'item18_price': str(*cursor.execute('SELECT price FROM Products WHERE id = 18').fetchone()),
    'item18_ref': str(*cursor.execute('SELECT ref FROM Products WHERE id = 18').fetchone()),

    'item19': str(*cursor.execute('SELECT name FROM Products WHERE id = 19').fetchone()),
    'item19_desc': str(*cursor.execute('SELECT description FROM Products WHERE id = 19').fetchone()),
    'item19_price': str(*cursor.execute('SELECT price FROM Products WHERE id = 19').fetchone()),
    'item19_ref': str(*cursor.execute('SELECT ref FROM Products WHERE id = 19').fetchone()),

    'item20': str(*cursor.execute('SELECT name FROM Products WHERE id = 20').fetchone()),
    'item20_desc': str(*cursor.execute('SELECT description FROM Products WHERE id = 20').fetchone()),
    'item20_price': str(*cursor.execute('SELECT price FROM Products WHERE id = 20').fetchone()),
    'item20_ref': str(*cursor.execute('SELECT ref FROM Products WHERE id = 20').fetchone()),

    'item21': str(*cursor.execute('SELECT name FROM Products WHERE id = 21').fetchone()),
    'item21_desc': str(*cursor.execute('SELECT description FROM Products WHERE id = 21').fetchone()),
    'item21_price': str(*cursor.execute('SELECT price FROM Products WHERE id = 21').fetchone()),
    'item21_ref': str(*cursor.execute('SELECT ref FROM Products WHERE id = 21').fetchone()),

    'item22': str(*cursor.execute('SELECT name FROM Products WHERE id = 22').fetchone()),
    'item22_desc': str(*cursor.execute('SELECT description FROM Products WHERE id = 22').fetchone()),
    'item22_price': str(*cursor.execute('SELECT price FROM Products WHERE id = 22').fetchone()),
    'item22_ref': str(*cursor.execute('SELECT ref FROM Products WHERE id = 22').fetchone()),

    # GAME DEVICES
    'item6': str(*cursor.execute('SELECT name FROM Products WHERE id = 6').fetchone()),
    'item6_desc': str(*cursor.execute('SELECT description FROM Products WHERE id = 6').fetchone()),
    'item6_price': str(*cursor.execute('SELECT price FROM Products WHERE id = 6').fetchone()),
    'item6_ref': str(*cursor.execute('SELECT ref FROM Products WHERE id = 6').fetchone()),

    # FURN
    'item7': str(*cursor.execute('SELECT name FROM Products WHERE id = 7').fetchone()),
    'item7_desc': str(*cursor.execute('SELECT description FROM Products WHERE id = 7').fetchone()),
    'item7_price': str(*cursor.execute('SELECT price FROM Products WHERE id = 7').fetchone()),
    'item7_ref': str(*cursor.execute('SELECT ref FROM Products WHERE id = 7').fetchone()),

}

connect.commit()
