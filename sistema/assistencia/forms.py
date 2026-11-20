from django import forms
from .models import Cliente, Aparelho, Agendamento
 
 
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nome", "cpf", "telefone", "email"]
 
 
class AparelhoForm(forms.ModelForm):
    class Meta:
        model = Aparelho
        fields = ["imei", "marca", "modelo", "ano", "cor", "cliente"]
 
 
class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ["data", "horario", "servico", "aparelho"]
        widgets = {
            "data": forms.DateInput(attrs={"type": "date"}),
            "horario": forms.TimeInput(attrs={"type": "time"}),
        }
 
 
class DataForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ["data"]
        widgets = {
            "data": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
        }

Ask AI
