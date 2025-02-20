import telebot
#from bot_logic import gen_pass, gen_emodji, flip_coin  # Импортируем функции из bot_logic
from model import get_class

# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("7830796741:AAEmZsGGjvaLzyDgDwZcChJ4s9c2iU9e9Oc")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши команду /hello, /bye, или просто обычный текст. Если хочешь узнать, что за заморскую птицу ты видел, просто прикрепи фото птицы (фото голубя или синицы)")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")


@bot.message_handler(content_types=['text', 'photo'])
def handle_docs_photo(message):
    # Проверяем, есть ли фотографии
    if not message.photo:
        return bot.send_message(message.chat.id, "Вы забыли загрузить картинку :(")
    
    if message.photo:
        # Получаем файл и сохраняем его
        file_info = bot.get_file(message.photo[-1].file_id)
        file_name = file_info.file_path.split('/')[-1]
        
        src='./ai_bot/'+file_info.file_path

        # Загружаем файл и сохраняем
        downloaded_file = bot.download_file(file_info.file_path)
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        
        result = get_class(model_path="./ai_bot/keras_model.h5", labels_path="./ai_bot/labels.txt", image_path=src)
        
        if result is None:
            bot.send_message(message.chat.id, 'Я сомневаюсь, что знаю, что на картинке, попробуйте использовать другую картинку')           
        else: 
            bot.send_message(message.chat.id, result)


# @bot.message_handler(content_types=['text', 'photo', 'sticker'])
# def handle_message(message):
  
#   # Ответ на текстовое сообщение
#   if message.text == 'Привет':
#       bot.send_message(message.chat.id, 'Привет! Как дела?')
  
#   # Ответ на изображение
#   if message.photo:
#       bot.send_message(message.chat.id, 'Вы отправили изображение.')
  
#   # Ответ на стикер
#   if message.sticker:
#       bot.send_message(message.chat.id, 'Вы отправили стикер.')

# Запускаем бота
bot.polling()





