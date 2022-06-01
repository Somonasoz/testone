import telebot
from telebot import types

import telebot
from telebot import types



TOKEN = '5157184442:AAGXaHzPtNdaUVAdr04zDBzknjBKx5JOpng'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton('🇹🇯 TJ')
    item2 = types.KeyboardButton('🇷🇺 RU')
    item3 = types.KeyboardButton('🇬🇧 EN')


    markup.add(item1, item2, item3, )

    bot.send_message(message.chat.id, 'Салом  {0.first_name} 👋. '' Пеш аз он ки оғоз намоем забони худро интихоб кунед!'.format(message.from_user), reply_markup=markup)




@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        # Точики ________________________________________________________________
        if message.text == '🇹🇯 TJ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('💵 Тавозун')
            item2 = types.KeyboardButton('📦 Тарофаи ман')
            item3 = types.KeyboardButton('🛍 Моби Пакетҳо')
            item4 = types.KeyboardButton('⚙ Хизматрасониҳо')
            #item5 = types.KeyboardButton('✉ Тамос бо оператор')
            back = types.KeyboardButton('🇹🇯 Забон')
            markup.add(item1, item2, item3, item4, back)

            bot.send_message(message.chat.id, '🇹🇯 TJ', reply_markup=markup)
# Тариф _________________________________________________________________

        elif message.text == '📦 Тарофаи ман':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('✅ Бале')
            item2 = types.KeyboardButton('❌ Намехоҳам')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Тарофаи шумо: " " Шумо мехоҳед тарофаи худро иваз намоед?',
                             reply_markup=markup)


        elif message.text == '✅ Бале':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('Бароҳат')
            item2 = types.KeyboardButton('Кайҳон 1')
            item3 = types.KeyboardButton('Кайҳон 2')
            item4 = types.KeyboardButton('Кайҳон 3')
            item5 = types.KeyboardButton('Кайҳон 4')
            item6 = types.KeyboardButton('Кайҳон 5')
            item7 = types.KeyboardButton('Гуфтугу 1')
            item8 = types.KeyboardButton('Гуфтугу 2')
            item9 = types.KeyboardButton('Гуфтугу 3')
            item10 = types.KeyboardButton('Гуфтугу 4')
            back = types.KeyboardButton('<< Ба оқиб')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, back)

            bot.send_message(message.chat.id, 'Шумо метавонед тарофаи худро иваз намоед.',
                             reply_markup=markup)

        elif message.text == '❌ Намехоҳам':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('💵 Тавозун')
            item2 = types.KeyboardButton('📦 Тарофаи ман')
            item3 = types.KeyboardButton('🛍 Моби Пакетҳо')
            item4 = types.KeyboardButton('⚙ Хизматрасониҳо')
            #item5 = types.KeyboardButton('✉ Тамос бо оператор')
            back = types.KeyboardButton('🇹🇯 Забон')
            markup.add(item1, item2, item3, item4,  back)

            bot.send_message(message.chat.id, 'Фасли зарури интихоб намуда маълумоти даркориро дастрас намоед.',
                             reply_markup=markup)

        elif message.text == '<< Ба оқиб':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('💵 Тавозун')
            item2 = types.KeyboardButton('📦 Тарофаи ман')
            item3 = types.KeyboardButton('🛍 Моби Пакетҳо')
            item4 = types.KeyboardButton('⚙ Хизматрасониҳо')
           # item5 = types.KeyboardButton('✉ Тамос бо оператор')
            back = types.KeyboardButton('🇹🇯 Забон')
            markup.add(item1, item2, item3, item4, back)

            bot.send_message(message.chat.id, 'Фасли зарури интихоб намуда маълумоти даркориро дастрас намоед.',
                             reply_markup=markup)


        # Кнопка Забон_________________________________________________________________
        elif message.text == '🇹🇯 Забон':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('🇹🇯 TJ')
            item2 = types.KeyboardButton('🇷🇺 RU')
            item3 = types.KeyboardButton('🇬🇧 EN')

            markup.add(item1, item2, item3, )

            bot.send_message(message.chat.id, '🇹🇯 Забон'.format(message.from_user), reply_markup=markup)

# Кнопка оператор точики_________________________________________________________________
        elif message.text == '✉ Тамос бо оператор':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('☎ Қатъи алоқа')

            markup.add(item1)

            bot.send_message(message.chat.id,
                             'Мушкилии худро нависен орератон дар наздиктарин вақт ба шумо қавоб хоҳад дод'.format(
                                 message.from_user), reply_markup=markup)

        elif message.text == '☎ Қатъи алоқа':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('💵 Тавозун')
            item2 = types.KeyboardButton('📦 Тарофаи ман')
            item3 = types.KeyboardButton('🛍 Моби Пакетҳо')
            item4 = types.KeyboardButton('⚙ Хизматрасониҳо')
            item5 = types.KeyboardButton('✉ Тамос бо оператор')
            back = types.KeyboardButton('🇹🇯 Забон')
            markup.add(item1, item2, item3, item4, item5, back)

            bot.send_message(message.chat.id, 'Фасли зарури интихоб намуда маълумоти даркориро дастрас намоед.',
                             reply_markup=markup)

        # Кнопка Моби Пакети точики_________________________________________________________________

        elif message.text == '↩ Аввал':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('💵 Тавозун')
            item2 = types.KeyboardButton('📦 Тарофаи ман')
            item3 = types.KeyboardButton('🛍 Моби Пакетҳо')
            item4 = types.KeyboardButton('⚙ Хизматрасониҳо')
            #item5 = types.KeyboardButton('✉ Тамос бо оператор')
            back = types.KeyboardButton('🇹🇯 Забон')
            markup.add(item1, item2, item3, item4,  back)

            bot.send_message(message.chat.id, 'Фасли зарури интихоб намуда маълумоти даркориро дастрас намоед', reply_markup=markup)


#market
# Моби Пакетиҳо___________________________________________________________

        elif message.text == '🛍 Моби Пакетҳо':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('МегаБайтҳо')
            item2 = types.KeyboardButton('Дақиқаҳо')
            item3 = types.KeyboardButton('СМС паёмакҳо')
            item4 = types.KeyboardButton('↩ Аввал')
            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id, '🛍 Моби Пакети', reply_markup=markup)



# МегаБайтҳо__________________________________________________________________

        elif message.text == 'МегаБайтҳо':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('Харидории Мегабайтҳо')
            item2 = types.KeyboardButton('Тавтиши Мегабайҳо')
            item3 = types.KeyboardButton('↩ Аввал')
            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, 'МегаБайтҳо', reply_markup=markup)



        elif message.text == 'Харидории Мегабайтҳо':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('250мб (9,93 сомони - 90 рӯз)')
            item2 = types.KeyboardButton('500мб (19,86 сомони - 90 рӯз)')
            item3 = types.KeyboardButton('1 000мб (34,75 сомони - 90 рӯз)')
            item4 = types.KeyboardButton('3 000мб (64,55сомони - 90 рӯз)')
            item5 = types.KeyboardButton('6 000мб (98,32 сомони - 90 рӯз)')
            item6 = types.KeyboardButton('10 000мб (158,90  сомони - 180 рӯз)')
            item7 = types.KeyboardButton('20 000мб (297,94 сомони  - 180 рӯз)')
            item8 = types.KeyboardButton('30 000мб (397,25 сомони  - 365 рӯз)')
            item9 = types.KeyboardButton('60 000мб (595,88 сомони - 365 рӯз)')
            item10 = types.KeyboardButton('↩ Аввал')


            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)

            bot.send_message(message.chat.id, 'МегаБайтҳо', reply_markup=markup)


 # Дақиқаҳо_________________________________________________________________________________






        elif message.text == 'Дақиқаҳо':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('Харидории Дақиқаҳо дохили шабака')
            item2 = types.KeyboardButton('Харидории Дақиқаҳо ҳамаи самтҳо')
            item3 = types.KeyboardButton('Тавтиши Дақиқаҳо')
            item4 = types.KeyboardButton('↩ Аввал')


            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id, 'Дақиқаҳо', reply_markup=markup)



        elif message.text == 'Харидории Дақиқаҳо дохили шабака':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('10 Дақика-0,86 сомонӣ')
            item2 = types.KeyboardButton('25 Дақика-2,15 сомонӣ')
            item3 = types.KeyboardButton('101 Дақика-5,79 сомонӣ')
            item4 = types.KeyboardButton('200 Дақика-11,48 сомонӣ')
            item5 = types.KeyboardButton('501 Дақика-14,32 сомонӣ')
            item10 = types.KeyboardButton('↩ Аввал')


            markup.add(item1, item2, item3, item4, item5, item10)

            bot.send_message(message.chat.id, 'Муҳлати дақиқаҳо 90-рӯз мебошад.', reply_markup=markup)



        elif message.text == 'Харидории Дақиқаҳо ҳамаи самтҳо':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('10 Дақика-2,29 сомонӣ')
            item2 = types.KeyboardButton('51 Дақика-10,23 сомонӣ')
            item3 = types.KeyboardButton('101 Дақика-18,53 сомонӣ')
            item4 = types.KeyboardButton('251 Дақика-44,6 сомонӣ')
            item5 = types.KeyboardButton('501 Дақика-86,22 сомонӣ')
            item5 = types.KeyboardButton('1001 Дақика-160,66 сомонӣ')
            item10 = types.KeyboardButton('↩ Аввал')

            markup.add(item1, item2, item3, item4, item5, item10)

            bot.send_message(message.chat.id, 'Муҳлати дақиқаҳо 90-рӯз мебошад.', reply_markup=markup)

# СМС паёмакҳо------------------------------------------------------------------------------------

        elif message.text == 'СМС паёмакҳо':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('Харидории СМС паёмакҳо дохили шабака')
            item2 = types.KeyboardButton('Харидории СМС паёмакҳо ҳамаи самтҳо')
            item3 = types.KeyboardButton('Тавтиши СМС паёмакҳо')
            item4 = types.KeyboardButton('↩ Аввал')

            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id, 'СМС паёмакҳо', reply_markup=markup)



        elif message.text == 'Харидории СМС паёмакҳо дохили шабака':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('10 паёмак (0,63 сомонӣ)')
            item2 = types.KeyboardButton('25 паёмак (1.57 сомонӣ)')
            item3 = types.KeyboardButton('100 паёмак (6.31 сомонӣ)')
            item4 = types.KeyboardButton('201 паёмак (9,20 сомонӣ)')
            item5 = types.KeyboardButton('501 паёмак (11.47 сомонӣ)')
            item10 = types.KeyboardButton('↩ Аввал')

            markup.add(item1, item2, item3, item4, item5, item10)

            bot.send_message(message.chat.id, 'Муҳлати СМС паёмак 90-рӯз мебошад.',
                             reply_markup=markup)


        elif message.text == 'Харидории СМС паёмакҳо ҳамаи самтҳо':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('10 паёмак (1.03 сомонӣ)')
            item2 = types.KeyboardButton('25 паёмак (2,58 сомонӣ)')
            item3 = types.KeyboardButton('100 паёмак (8,69 сомонӣ)')
            item4 = types.KeyboardButton('201 паёмак (13,82 сомонӣ)')
            item5 = types.KeyboardButton('501 паёмак (23,49 сомонӣ)')
            item10 = types.KeyboardButton('↩ Аввал')

            markup.add(item1, item2, item3, item4, item5, item10)

            bot.send_message(message.chat.id, 'нархнома СМС паёмакҳо ҳамаи самтҳо---''--------''--------',
                             reply_markup=markup)

# Хизматрасонихо------------------------------------------------------------------------------------
        elif message.text == '⚙ Хизматрасониҳо':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('Smart+')
            item2 = types.KeyboardButton('Рангоранг')
            item3 = types.KeyboardButton('Роҳнамо')
            item4 = types.KeyboardButton('Пешрав')
            item5 = types.KeyboardButton('MobiZero')
            item6 = types.KeyboardButton('Моби-Конструктор')
            #item7 = types.KeyboardButton('Mobi-Active')
            item8 = types.KeyboardButton('↩ Аввал')

            markup.add(item1, item2, item3, item4, item5, item6,item8)

            bot.send_message(message.chat.id, '⚙ Хизматрасониҳои', reply_markup=markup)

#Smart +__________________________________________________________________________

        elif message.text == 'Smart+':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('Пайваст намудан')
            item2 = types.KeyboardButton('Хомуш кардан')
            item10 = types.KeyboardButton('↩ Аввал')

            markup.add(item1, item2, item10)

            bot.send_message(message.chat.id, 'Арзиши хизматрасонӣ: 1,29 сомонӣ/рӯз.',reply_markup=markup)

# Рангоранг__________________________________________________________________________

        elif message.text == 'Рангоранг':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('Пайваст намудан Рангоранг')
            item2 = types.KeyboardButton('Хомуш кардан Рангоранг')
            item10 = types.KeyboardButton('↩ Аввал')

            markup.add(item1, item2, item10)

            bot.send_message(message.chat.id,
                             '1 GB + ♾ Messengers: Telegram, WhastApp, Imo, Viber, MobiГап, WeChat,QQ Бемаҳдуд мебошад. Арзиши хизматрасонӣ: 28,80 сомонӣ',
                             reply_markup=markup)

#Рохнамо__________________________________________________________________________

        elif message.text == 'Роҳнамо':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('Пайваст намудан Рохнамо')
            item2 = types.KeyboardButton('Хомуш кардан Рохнамо')
            item10 = types.KeyboardButton('↩ Аввал')

            markup.add(item1, item2, item10)

            bot.send_message(message.chat.id, '2 GB + ♾ Шабакаҳои иштимои: Instagram, Facebook, OK, Vkontakte, Twitter ♾ Messengers:  Facebook Messenger,Telegram, WhastApp, Imo, Viber, MobiГап, WeChat,QQ Бемаҳдуд мебошад. Арзиши хизматрасонӣ: 58,59 сомонӣ', reply_markup=markup)

# Пешрав__________________________________________________________________________

        elif message.text == 'Пешрав':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('Пайваст намудан Пешрав')
            item2 = types.KeyboardButton('Хомуш кардан Пешрав')
            item10 = types.KeyboardButton('↩ Аввал')

            markup.add(item1, item2, item10)

            bot.send_message(message.chat.id, '3 GB + ♾ Шабакаҳои иштимои: YouTube, Instagram, Facebook, OK, Vkontakte, Twitter ♾ Messengers: Facebook Messenger, Telegram, WhastApp, Imo, Viber, MobiГап, WeChat,QQ Бемаҳдуд мебошад. Арзиши хизматрасонӣ: 58,59 сомонӣ',
                             reply_markup=markup)

# MobiZero__________________________________________________________________________

        elif message.text == 'MobiZero':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('MobiZero Тоҷикистон')
            item2 = types.KeyboardButton('MobiZero Суғд')
            item3 = types.KeyboardButton('MobiZero Хатлон')
            item4 = types.KeyboardButton('MobiZero ВМКБ')
            item10 = types.KeyboardButton('↩ Аввал')

            markup.add(item1, item2, item3, item4, item10)

            bot.send_message(message.chat.id,
                             'MobiZero Бемаҳдуд дар дохилӣ шабака.', reply_markup=markup)
# MobiZero Тоҷикистон__________________________________________________________________________

        elif message.text == 'MobiZero Тоҷикистон':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('1 Рӯза')
            item2 = types.KeyboardButton('1 Моҳ')
            item10 = types.KeyboardButton('↩ Аввал')

            markup.add(item1, item2, item10)

            bot.send_message(message.chat.id,
                             'MobiZero Тоҷикистон', reply_markup=markup)
# MobiZero Тоҷикистон 1 Рӯза__________________________________________________________________________

        elif message.text == '1 Рӯза':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('1 Рӯза пайвваст намудан')
            item2 = types.KeyboardButton('1 Рӯза хомуш намудан')
            item10 = types.KeyboardButton('↩ Аввал')

            markup.add(item1, item2, item10)

            bot.send_message(message.chat.id,'MobiZero Тоҷикистон. 1 Рӯза Арзиши хизматрасонӣ: 0,79 сомонӣ/рӯз.', reply_markup=markup)

# MobiZero Тоҷикистон 1 Моҳ__________________________________________________________________________

        elif message.text == '1 Моҳ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('1 Моҳ пайвваст намудан')
            item2 = types.KeyboardButton('1 Моҳ хомуш намудан')
            item10 = types.KeyboardButton('↩ Аввал')

            markup.add(item1, item2, item10)

            bot.send_message(message.chat.id,
                             'MobiZero Тоҷикистон 1 Моҳ. Арзиши хизматрасонӣ: 14.70 сомонӣ/моҳ.', reply_markup=markup)

# MobiZero MobiZero Суғд__________________________________________________________________________

        elif message.text == 'MobiZero Суғд':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('MobiZero Суғд пайвваст намудан')
            item2 = types.KeyboardButton('MobiZero Суғд хомуш намудан')
            item10 = types.KeyboardButton('↩ Аввал')

            markup.add(item1, item2, item10)

            bot.send_message(message.chat.id, 'MobiZeroMobiZero Суғд. Арзиши хизматрасонӣ: 0.60 сомонӣ/рӯз.', reply_markup=markup)

# MobiZero MobiZero Хатлон__________________________________________________________________________

        elif message.text == 'MobiZero Хатлон':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('MobiZero Хатлон пайвваст намудан')
            item2 = types.KeyboardButton('MobiZero Хатлон хомуш намудан')
            item10 = types.KeyboardButton('↩ Аввал')

            markup.add(item1, item2, item10)

            bot.send_message(message.chat.id, 'MobiZero Хатлон нархнома. Арзиши хизматрасонӣ: 0.60 сомонӣ/рӯз.', reply_markup=markup)

# MobiZero MobiZero ВМКБ__________________________________________________________________________

        elif message.text == 'MobiZero ВМКБ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('MobiZero ВМКБ пайвваст намудан')
            item2 = types.KeyboardButton('MobiZero ВМКБ хомуш намудан')
            item10 = types.KeyboardButton('↩ Аввал')

            markup.add(item1, item2, item10)

            bot.send_message(message.chat.id, 'MobiZero ВМКБ  нархнома. Арзиши хизматрасонӣ: 0.60 сомонӣ/рӯз.', reply_markup=markup)

# Моби-Конструктор__________________________________________________________________________

        elif message.text == 'Моби-Конструктор':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('Mobi - Конструктор 1')
            item2 = types.KeyboardButton('Mobi - Конструктор 2')
            item3 = types.KeyboardButton('Mobi - Конструктор 3')
            #item4 = types.KeyboardButton('MobiTURBO 1000')
            item10 = types.KeyboardButton('↩ Аввал')

            markup.add(item1, item2, item3, item10)

            bot.send_message(message.chat.id,
                             'Моби-Конструктор', reply_markup=markup)

# Mobi - Конструктор 1__________________________________________________________________________

        elif message.text == 'Mobi - Конструктор 1':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('Mobi - Конструктор 1 пайвваст намудан')
            item2 = types.KeyboardButton('Mobi - Конструктор 1 намудан')
            item10 = types.KeyboardButton('↩ Аввал')

            markup.add(item1, item2, item10)

            bot.send_message(message.chat.id, 'Mobi - Конструктор 1 Шумораи дақиқа ба ҳама самтҳои дохили ҶТ: 50   Миқдори SMS ба ҳамаи самтҳои ҶТ: 50  Миқдори Мегабайт: 100 Арзиши хизматрасонӣ: 7,94 сомонӣ ', reply_markup=markup)

# MobiZero MobiTURBO 100__________________________________________________________________________

        elif message.text == 'Mobi - Конструктор 2':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('Mobi - Конструктор 2 пайвваст намудан')
            item2 = types.KeyboardButton('Mobi - Конструктор 2 хомуш намудан')
            item10 = types.KeyboardButton('↩ Аввал')

            markup.add(item1, item2, item10)

            bot.send_message(message.chat.id, 'Mobi - Конструктор 2 Шумораи дақиқа ба ҳама самтҳои дохили ҶТ: 100   Миқдори SMS ба ҳамаи самтҳои ҶТ: 100 Миқдори Мегабайт: 200 Арзиши хизматрасонӣ: 14,89 сомонӣ ', reply_markup=markup)

# MobiZero MobiTURBO 500__________________________________________________________________________

        elif message.text == 'Mobi - Конструктор 3':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('Mobi - Конструктор 3 пайвваст намудан')
            item2 = types.KeyboardButton('Mobi - Конструктор 3 хомуш намудан')
            item10 = types.KeyboardButton('↩ Аввал')

            markup.add(item1, item2, item10)

            bot.send_message(message.chat.id, 'Конструктор 3 Шумораи дақиқа ба ҳама самтҳои дохили ҶТ: 150   Миқдори SMS ба ҳамаи самтҳои ҶТ: 150  Миқдори Мегабайт: 200 Арзиши хизматрасонӣ: 22,84 сомонӣ', reply_markup=markup)

# MobiZero MobiTURBO 1000__________________________________________________________________________

        elif message.text == 'MobiTURBO 1000':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('MobiTURBO 1000 пайвваст намудан')
            item2 = types.KeyboardButton('MobiTURBO 1000 хомуш намудан')
            item10 = types.KeyboardButton('↩ Аввал')

            markup.add(item1, item2, item10)

            bot.send_message(message.chat.id, 'Mobi - Конструктор 3 нархнома 5,70 ''--------', reply_markup=markup)

# Mobi Mobi-Active__________________________________________________________________________

        elif message.text == 'Mobi-Active':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('Mobi-Active 1')
            item2 = types.KeyboardButton('Mobi-Active 2')

            item10 = types.KeyboardButton('↩ Аввал')

            markup.add(item1, item2,  item10)

            bot.send_message(message.chat.id,
                             'Mobi-Active ---''--------', reply_markup=markup)

# MobiZero Mobi-Active 1_________________________________________________________________________

        elif message.text == 'Mobi-Active 1':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('Mobi-Active 1 пайвваст намудан')
            item2 = types.KeyboardButton('Mobi-Active 1 хомуш намудан')
            item10 = types.KeyboardButton('↩ Аввал')

            markup.add(item1, item2, item10)

            bot.send_message(message.chat.id, 'Mobi-Active 1 нархнома 6,70 ''--------', reply_markup=markup)

        # MobiZero Mobi-Active 2__________________________________________________________________________

        elif message.text == 'Mobi-Active 2':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('Mobi-Active 2 пайвваст намудан')
            item2 = types.KeyboardButton('Mobi-Active 2 хомуш намудан')
            item10 = types.KeyboardButton('↩ Аввал')

            markup.add(item1, item2, item10)

            bot.send_message(message.chat.id, 'Mobi-Active 2 нархнома 5,70 ''--------', reply_markup=markup)








        #  Русси_________________________________________________________________
        elif message.text == '🇷🇺 RU':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('💵 Баланс')
            item2 = types.KeyboardButton('📦 Мой тариф')
            item3 = types.KeyboardButton('🛍 Моbi Пакети')
            item5 = types.KeyboardButton('⚙ Услуги')
            #item4 = types.KeyboardButton('✉ Связаться с оператором')
            back = types.KeyboardButton('🇷🇺 Язык')
            markup.add(item1, item2, item3,item5, back)

            bot.send_message(message.chat.id, '🇷🇺 RU', reply_markup=markup)

        # Кнопка оператор руси_________________________________________________________________
        elif message.text == '✉ Связаться с оператором':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('☎ Прерывание связи')

            markup.add(item1)

            bot.send_message(message.chat.id,
                             'Напишите свой вопрос оператор ответит вам в ближайшее время'.format(message.from_user),
                             reply_markup=markup)

        elif message.text == '☎ Прерывание связи':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('💵 Баланс')
            item2 = types.KeyboardButton('📦 Мой тариф')
            item3 = types.KeyboardButton('🛍 Мом Пакети')
            item5 = types.KeyboardButton('⚙ Услуги')
            #item4 = types.KeyboardButton('✉ Связаться с оператором')
            back = types.KeyboardButton('🇷🇺 Язык')
            markup.add(item1, item2, item3, item5, back)

            bot.send_message(message.chat.id, 'Выберите соответствующий раздел и получите необходимую информацию.',
                             reply_markup=markup)

        # Кнопка Язык_________________________________________________________________
        elif message.text == '🇷🇺 Язык':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('🇹🇯 TJ')
            item2 = types.KeyboardButton('🇷🇺 RU')
            item3 = types.KeyboardButton('🇬🇧 EN')

            markup.add(item1, item2, item3, )

            bot.send_message(message.chat.id, '🇷🇺 Язык'.format(message.from_user), reply_markup=markup)


        # English_________________________________________________________________
        elif message.text == '🇬🇧 EN':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('💵 Balans')
            item2 = types.KeyboardButton('📦 Tarifs')
            item3 = types.KeyboardButton('🛍 Pakets')
            item5 = types.KeyboardButton('⚙ Services')
            #item4 = types.KeyboardButton('✉ Contact the operator')
            back = types.KeyboardButton('🇬🇧 Language')
            markup.add(item1, item2, item3, item5, back)

            bot.send_message(message.chat.id, '🇬🇧 EN', reply_markup=markup)

        # Кнопка оператор English_________________________________________________________________
        elif message.text == '✉ Contact the operator':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('☎ Interruption of communication')

            markup.add(item1)

            bot.send_message(message.chat.id,
                             'Write your question the operator will answer you soon'.format(message.from_user),
                             reply_markup=markup)



        elif message.text == '☎ Interruption of communication':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('💵 Balans')
            item2 = types.KeyboardButton('📦 Tarifs')
            item3 = types.KeyboardButton('🛍 Pakets')
            item5 = types.KeyboardButton('⚙ Services')
            #item4 = types.KeyboardButton('✉ Contact the operator')
            back = types.KeyboardButton('🇬🇧 Language')
            markup.add(item1, item2, item3, item5, back)

            bot.send_message(message.chat.id, 'Select the appropriate section and get the necessary information',
                             reply_markup=markup)




        # Кнопка Language_________________________________________________________________
        elif message.text == '🇬🇧 Language':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('🇹🇯 TJ')
            item2 = types.KeyboardButton('🇷🇺 RU')
            item3 = types.KeyboardButton('🇬🇧 EN')

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, '🇬🇧 Language'.format(message.from_user), reply_markup=markup)



bot.polling(none_stop=True)