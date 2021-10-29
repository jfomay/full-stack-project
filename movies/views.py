from django.shortcuts import render, get_object_or_404
from movies.models import Movie
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def list(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/list.html', context)

def detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    context = {
        'movie': movie
    }
    return render(request, 'movies/detail.html', context)

def create(request):
    if request.method == 'POST':
        title = request.POST['title'] 
        date_released = request.POST['date_released']
        
        Movie.objects.create(title=title, date_released=date_released)
        return HttpResponseRedirect(reverse('movies_list'))
    else:
        return render(request, 'movies/create.html')

def update(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == 'POST':
        title = request.POST['title'] 
        date_released = request.POST['date_released']

        movie.title = title
        movie.date_released = date_released
        movie.save()
        return HttpResponseRedirect(reverse('movie_detail', kwargs={'movie_id': movie.id}))
    else:
        d = movie.date_released
        date_released = f'{d.year}-{d.month:02d}-{d.day}'

        context = {
            'movie': movie,
            'date_released': date_released
        }
        return render(request, 'movies/update.html', context)

