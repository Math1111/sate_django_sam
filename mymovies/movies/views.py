#views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

# Существующее представление списка фильмов
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})


# Новое представление для страницы с подробностями фильма
@login_required  # Ограничиваем доступ только авторизованным пользователям

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    ##comments = movie.comments.all()  # Получаем все комментарии для этого фильма
    comments = movie.comments.exclude(text__isnull=True).exclude(text="")
    #average_rating = movie.average_rating()
    average_rating = movie.comments.aggregate(Avg('rating'))['rating__avg']
    ##movie.comments.aggregate(Avg('rating'))['rating__avg']

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie  # Привязываем комментарий к фильму
            comment.user = request.user  # Привязываем комментарий к текущему пользователю
            comment.save()
            return redirect('movie_detail', movie_id=movie.id)  # Перезагружаем страницу с новым комментарием
        else:
            print(form.errors)
    else:
        form = CommentForm()  # Пустая форма, если GET-запрос


    return render(request, 'movies/movie_detail.html', {
        'movie': movie,
        'comments': comments,
        'form': form,
        'average_rating': movie.average_rating(),
    })