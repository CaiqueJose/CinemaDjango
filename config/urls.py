from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name = "index"),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('pessoas/', PessoasView.as_view(), name = "pessoas"),
    path('cursos/', CursosView.as_view(), name = "cursos"),
    path('instituicoes/', InstituicoesView.as_view(), name = "instituicoes"),
    path('areas/', AreasView.as_view(), name = "areas"),
    path('disciplinas/', DisciplinasView.as_view(), name = "disciplinas"),
    path('matriculas/', MatriculasView.as_view(), name = "matriculas"),
    path('frequencias/', FrequenciasView.as_view(), name = "frequencias"),
    path('ocorrencias/', OcorrenciasView.as_view(), name = "ocorrencias"),

]