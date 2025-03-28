from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=255)  # Название фильма
    description = models.TextField()  # Описание фильма
    image = models.ImageField(upload_to='movies/')  # Картинка фильма

    def average_rating(self):
        ratings = self.comments.values_list('rating', flat=True)  # Получаем все оценки
        return round(sum(ratings) / len(ratings), 1) if ratings else None

    def __str__(self):
        return self.title

class Comment(models.Model):#
    movie = models.ForeignKey(Movie, related_name='comments', on_delete=models.CASCADE)  # Привязка к фильму#
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Привязка к пользователю#
    text = models.TextField(blank=True, null=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания#

    def __str__(self):#
        return f"Comment by {self.user.username} on {self.movie.title}"#
