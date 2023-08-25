from django import forms
from dci.models import DciGerada


class DciForms (forms.ModelForm):
    class Meta:
        model = DciGerada
        fields = '__all__'
