from django import forms
from ..models.category import Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length = 130, help_text = 'Nome da categoria: ')
    comments = forms.CharField(widget = forms.Textarea(),max_length = 600, help_text = 'Comente: ')
    views = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
    likes = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
    slug = forms.CharField(widget = forms.HiddenInput, required = False)

    class Meta:
        model = Category
        fields = ('name', 'comments',)