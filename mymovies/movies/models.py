from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)  # Название фильма
    description = models.TextField()  # Описание фильма
    image = models.ImageField(upload_to='movies/')  # Картинка фильма

    def __str__(self):
        return self.title
