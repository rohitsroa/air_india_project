from django import forms
from pages.models import QueryInfo

class QueryInfoForms(forms.ModelForm):
    class Meta:
        model = QueryInfo
        fields = "__all__"