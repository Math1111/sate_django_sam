#mymovies/movies/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('movie_list')

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})


@login_required

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    ##comments = movie.comments.all()
    comments = movie.comments.exclude(text__isnull=True).exclude(text="")
    #average_rating = movie.average_rating()
    average_rating = movie.comments.aggregate(Avg('rating'))['rating__avg']
    ##movie.comments.aggregate(Avg('rating'))['rating__avg']

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()
            return redirect('movie_detail', movie_id=movie.id)
        else:
            print(form.errors)
    else:
        form = CommentForm()


    return render(request, 'movies/movie_detail.html', {
        'movie': movie,
        'comments': comments,
        'form': form,
        'average_rating': movie.average_rating(),
    })