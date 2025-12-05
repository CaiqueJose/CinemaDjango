from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import Filme
from django import forms

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(FilmeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'nome',
            'duracao',
            'sinopse',
            'site_oficial',
            'data_lancamento',
            'nota_avaliacao',
            'genero',
            'pais',
            'diretor',
            Submit('submit', 'Salvar')
)