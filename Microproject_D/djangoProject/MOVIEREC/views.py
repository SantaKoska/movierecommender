from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import GenreForm
from .models import Genrecinema

def front(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            genre = form.cleaned_data['genre']
            movies = Genrecinema.objects.filter(Genre=genre)

            template = loader.get_template('firstpage.html')
            context = {'form': form, 'movies': movies}
            return HttpResponse(template.render(context, request))
    else:
        form = GenreForm()

    template = loader.get_template('firstpage.html')
    context = {'form': form}
    return HttpResponse(template.render(context, request))

