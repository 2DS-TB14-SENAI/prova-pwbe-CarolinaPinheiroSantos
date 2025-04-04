from django import forms
from .models import Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'

escolhas = (
    ("CAR", "cardiologista" ),
    ("ORT", "ortopedista"),
    ("GIN", "ginecologista"))

class EscolhasSearchForm(forms.Form):
    status = forms.ChoiceField(choices=escolhas)