from django.db import models

class areaSaber(models.Model):
    nome = models.CharField(max_length= 100, verbose_name= "Nome da Área")
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Área"
        verbose_name_plural = "Áreas"

class Ocupacao(models.Model):
    nome = models.CharField(max_length= 100, verbose_name= "Nome da Ocupação")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"
        
class Periodo(models.Model):
    nome = models.CharField(max_length= 100, verbose_name= "Nome do Período")
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Período"
        verbose_name_plural = "Períodos"
        
class tipoAvaliacao(models.Model):
    nome = models.CharField(max_length= 100, verbose_name= "Nome do Tipo")
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"
        
class Turma(models.Model):
    nome = models.CharField(max_length= 100, verbose_name= "Nome da Turma")
    turno = models.CharField(verbose_name= "Turno", max_length=100)
    
    def __str__(self):
        return f"{self.nome}, {self.turno}"
    
    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"
        
class Cidade(models.Model):
    nome = models.CharField(max_length= 100, verbose_name= "Nome da Cidade")
    uf = models.CharField(max_length= 2, verbose_name= "Uf do Estado")
    
    def __str__(self):
        return f"{self.nome}, {self.uf}"
    
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"
        
class Disciplina(models.Model):
    nome = models.CharField(max_length= 100, verbose_name= "Nome da Disciplina")
    areaSaber = models.ForeignKey(areaSaber, verbose_name= "Área do Saber", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"

        
class Instituicao(models.Model):
    nome = models.CharField(max_length= 100, verbose_name= "Nome da Instituição")
    site = models.CharField(max_length= 100, verbose_name= "Site")
    telefone = models.CharField(max_length= 100, verbose_name= "Telefone")
    cidade = models.ForeignKey(Cidade, on_delete= models.CASCADE, verbose_name= 'Cidade')
    
    def __str__(self):
        return f"{self.nome}, {self.cidade}"
    
    class Meta:
        verbose_name = "Instituição"
        verbose_name_plural = "Instituições"


class Pessoa(models.Model):
    nome = models.CharField(max_length= 100, verbose_name= 'Nome do Aluno')
    nome_pai = models.CharField(max_length= 100, verbose_name= 'Nome do Pai')
    nome_mae = models.CharField(max_length= 100, verbose_name= 'Nome da Mãe')
    cpf = models.IntegerField(verbose_name= 'CPF')
    data_nasc = models.DateField(verbose_name= 'Data de Nascimento')
    email = models.CharField(max_length= 100, verbose_name= 'E-mail')
    cidade = models.ForeignKey(Cidade, on_delete= models.CASCADE, verbose_name= 'Cidade')
    ocupacao = models.ForeignKey(Ocupacao, on_delete= models.CASCADE, verbose_name= 'Ocupação')
    
    def __str__(self):
        return f"{self.nome}, {self.cpf}"
    
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

class Curso(models.Model):
    nome = models.CharField(max_length= 100, verbose_name= 'Nome do Curso')
    carga_horaria_total = models.IntegerField(verbose_name= "Carga Horária Total")
    duracao_meses = models.IntegerField(verbose_name= "Duração")
    areaSaber = models.ForeignKey(areaSaber, verbose_name= "Área do Saber", on_delete=models.CASCADE)
    instituicao = models.ForeignKey(Instituicao, verbose_name= "Instituição", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nome}, {self.instituicao}"
    
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        
class Ocorrencia(models.Model):
    descricao = models.CharField(verbose_name= "Descrição", max_length=100)
    data = models.DateField(verbose_name= "Data da Ocorrência")
    curso = models.ForeignKey(Curso, verbose_name= "Curso", on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, verbose_name= "Disciplina", on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, verbose_name= "Pessoa", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pessoa}, {self.disciplina}"
    
    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"
        
class Avaliacao(models.Model):
    descricao = models.CharField(verbose_name= "Descrição", max_length=100)
    curso = models.ForeignKey(Curso, verbose_name= "Curso", on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, verbose_name= "Disciplina", on_delete=models.CASCADE)
    avaliacaoTipo = models.ForeignKey(tipoAvaliacao ,verbose_name= "Tipo de Avaliação", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.curso}, {self.disciplina}"
    
    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
        
class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, verbose_name= "Curso", on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, verbose_name= "Disciplina", on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, verbose_name= "Pessoa", on_delete=models.CASCADE)
    numero_faltas = models.IntegerField(verbose_name= "Número de Faltas")
    
    def __str__(self):
        return f"{self.pessoa}, {self.disciplina}"
    
    class Meta:
        verbose_name = "Frequência"
        verbose_name_plural = "Frequências"
        
class Matricula(models.Model):
    instituicao = models.ForeignKey(Instituicao, verbose_name= "Instituição", on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, verbose_name= "Curso", on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, verbose_name= "Pessoa", on_delete=models.CASCADE)
    data_inicio = models.IntegerField(verbose_name= "Data de Início")
    previsao_termino = models.IntegerField(verbose_name= "Data de Previsão de Término")
    
    def __str__(self):
        return f"{self.pessoa}, {self.curso}"
    
    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"
        

        