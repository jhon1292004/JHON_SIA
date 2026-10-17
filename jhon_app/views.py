from django.shortcuts import render, redirect, get_object_or_404
from .models import MovieVerse
from .forms import MovieVerseForm


# ---------------------------------------------------------
# MOVIE LIST + ADD
# Ang page nga nagpakita sa list sa movies ug nag-handle sa "Add movie"
# ---------------------------------------------------------
def movie_anime(request):
    if request.method == 'POST':
        # Kung nag-submit og form (Add movie)
        form = MovieVerseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_anime')
    else:
        # Kung nag-open ra sa page, empty form
        form = MovieVerseForm()

    # Kuhaon tanang movies gikan sa database
    movies = MovieVerse.objects.all()

    context = {
        'movie_anime': movies,
        'form': form,
    }
    return render(request, 'MovieVerse/movie_verse.html', context)


# ---------------------------------------------------------
# EDIT MOVIE
# Kuhaon ang movie base sa pk (ID), i-update kung nag-submit
# ---------------------------------------------------------
def edit_movie(request, pk):
    # Kung wala nay ingon nga ID, mugawas ang 404 page
    movie = get_object_or_404(MovieVerse, pk=pk)

    if request.method == 'POST':
        # instance=movie para i-update ang existing, dili maghimo og bag-o
        form = MovieVerseForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_anime')
    else:
        # Ipakita ang form nga naay existing data na
        form = MovieVerseForm(instance=movie)

    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'MovieVerse/edit_movie.html', context)


# ---------------------------------------------------------
# DELETE MOVIE
# POST ra ang gitugotan para dili ma-delete bisan sayop og click sa link
# ---------------------------------------------------------
def delete_movie(request, pk):
    movie = get_object_or_404(MovieVerse, pk=pk)

    if request.method == 'POST':
        movie.delete()

    return redirect('movie_anime')