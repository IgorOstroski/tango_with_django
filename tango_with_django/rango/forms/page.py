from django import forms
from ..models.page import Page


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length = 130, help_text = 'Coloque o titulo da pagina: ')
    url = forms.URLField(max_length = 200, help_text = 'Coloque a URL da pagina: ')
    views = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)

    class Meta:
        model = Page
        exclude = ('category',)
