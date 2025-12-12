from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages
# from .forms import EscolaForm

class IndexView(View):
    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.all()
        return render(request, "index.html", {"cursos": cursos})
    
class PessoasView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        return render(request, "pessoas.html", {"pessoas": pessoas})
    
class CursosView(View):
    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.all()
        return render(request, "cursos.html", {"cursos": cursos})
    
class InstituicoesView(View):
    def get(self, request, *args, **kwargs):
        instituicoes = Instituicao.objects.all()
        return render(request, "instituicoes.html", {"instituicoes": instituicoes})

class AreasView(View):
    def get(self, request, *args, **kwargs):
        areas = areaSaber.objects.all()
        return render(request, "areas.html", {"areas": areas})
    
class DisciplinasView(View):
    def get(self, request, *args, **kwargs):
        disciplinas = Disciplina.objects.all()
        return render(request, "disciplinas.html", {"disciplinas": disciplinas})
    
class MatriculasView(View):
    def get(self, request, *args, **kwargs):
        matriculas = Matricula.objects.all()
        return render(request, "matriculas.html", {"matriculas": matriculas})
    
class FrequenciasView(View):
    def get(self, request, *args, **kwargs):
        frequencias = Frequencia.objects.all()
        return render(request, "frequencias.html", {"frequencias": frequencias})
    
class OcorrenciasView(View):
    def get(self, request, *args, **kwargs):
        ocorrencias = Ocorrencia.objects.all()
        return render(request, "ocorrencias.html", {"ocorrencias": ocorrencias})