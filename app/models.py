from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length= 100, verbose_name= "Nome do Gênero")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"

class Filme(models.Model):
    nome = models.CharField(max_length= 100, verbose_name= "Nome do Filme")
    duracao = models.IntegerField(verbose_name= "Duração do Filme")
    sinopse = models.CharField(max_length = 100, verbose_name= "Sinópse")
    site_oficial = models.CharField(max_length= 100 ,verbose_name= "Site do Filme")
    data_lancamento = models.DateField(verbose_name= "Data de Lançamento")
    nota_avaliacao = models.FloatField(verbose_name= "Avaliação do Filme")
    genero = models.ForeignKey(Genero, on_delete= models.CASCADE, verbose_name= "Gênero do Filme")
    pais = models.ForeignKey(Pais, on_delete= models.CASCADE, verbose_name= "Pais do Filme")
    diretor = models.ForeignKey(Diretor, on_delete= models.CASCADE, verbose_name= "Diretor do Filme")
    def __str__(self):
        return f"{self.nome}, {self.data_lancamento}"
    class Meta:
        verbose_name = "Filme"
        verbose_name_plural = "Filmes"
        