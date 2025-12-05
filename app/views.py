from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class FilmesView(View):
    def get(self, request, *args, **kwargs):
        filmes = Filme.objects.all()
        return render(request, 'filmes.html', {'filmes': filmes})
# def post(self, request, *args, **kwargs):
class SeriesView(View):
    def get(self, request, *args, **kwargs):
        series = Serie.objects.all()
        return render(request, 'series.html', {'series': series})

class EpisodiosView(View):
    def get(self, request, *args, **kwargs):
        episodios = Episodio.objects.all()
        return render(request, 'episodios.html', {'episodios': episodios})
class GenerosView(View):
    def get(self, request, *args, **kwargs):
        generos = Genero.objects.all()
        return render(request, 'generos.html', {'generos': generos})
class TemporadasView(View):
    def get(self, request, *args, **kwargs):
        temporadas = Temporada.objects.all()
        return render(request, 'temporadas.html', {'temporadas': temporadas})
class ElencoView(View):
    def get(self, request, *args, **kwargs):
        elencos = Elenco.objects.all()
        return render(request, 'elenco.html', {'elencos': elencos})
class AtuacaoView(View):
    def get(self, request, *args, **kwargs):
        atuacoes = Atuacao.objects.all()
        return render(request, 'atuacoes.html', {'atuacoes': atuacoes})