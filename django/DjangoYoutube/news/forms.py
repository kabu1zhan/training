from django import  forms
class TestForm(forms.Form):
    Otziv = forms.CharField(help_text="Введите имя", max_length=15)
