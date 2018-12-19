from django import forms
from ..models.page import Category, Page

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length = 130, help_text = 'Nome da categoria: ')
    views = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
    url = forms.URLField(help_text='Insira a URL: ')
    category = forms.ModelChoiceField(queryset = Category.objects.all(), help_text = 'Escolha uma categoria: ')


    class Meta:
        model = Page
        fields = ('title','url','category',)