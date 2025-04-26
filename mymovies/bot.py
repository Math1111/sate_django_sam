from telegram import Update, InputMediaPhoto
from telegram.ext import Updater, CommandHandler, CallbackContext
import django
import os
from django.conf import settings
import logging
logging.basicConfig(level=logging.INFO)

# Настройка Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mymovies.settings")
django.setup()

from django.contrib.auth.models import User
from movies.models import Movie, Comment

TOKEN = '7756588287:AAFmUnQ701mMvWrHGrKB0OUL4Tn7-VLQThU'


def start(update: Update, context: CallbackContext):
    args = context.args
    if not args:
        update.message.reply_text("Привет! Чтобы авторизоваться, перейди в бота со ссылки с сайта.")
        return

    user_id = args[0]
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        update.message.reply_text("Пользователь не найден.")
        return

    update.message.reply_text(f"Привет, {user.username}! 🎬 Вот информация из твоего аккаунта:")

    movies = Movie.objects.all()

    if not movies.exists():
        update.message.reply_text("Фильмов пока нет.")
        return

    for movie in movies:
        # Полный URL к изображению
        image_url = f"{settings.BASE_URL}{movie.image.url}"

        # Текст сообщения
        text = f"🎬 {movie.title}\n⭐ Средняя оценка: {movie.average_rating() or 'Нет'}"

        # Получаем комментарий пользователя
        comment = Comment.objects.filter(user=user, movie=movie).last()
        if comment and comment.text:
            text += f"\n💬 Твой комментарий: {comment.text}"
        elif comment:
            text += f"\n🗳 Ты уже поставил оценку ({comment.rating})"

        try:
            # Вариант 1: Через URL (должен быть доступен из интернета)
            image_url = f"{settings.BASE_URL}{movie.image.url}"
            context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=image_url,
                caption=text
            )
        except Exception as e:
            print(f"URL отправка не удалась: {e}")
            try:
                # Вариант 2: Через локальный файл
                with open(movie.image.path, 'rb') as photo:
                    context.bot.send_photo(
                        chat_id=update.effective_chat.id,
                        photo=photo,
                        caption=text
                    )
            except Exception as e:
                print(f"Файловая отправка не удалась: {e}")
                update.message.reply_text(text)


updater = Updater(TOKEN)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
print("🤖 Бот запущен!")
updater.start_polling()
updater.idle()
