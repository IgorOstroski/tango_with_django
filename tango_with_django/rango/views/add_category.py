from django.shortcuts import render
from ..forms.category_form import CategoryForm
from .index import index

def add_category(request):
    if request.method =='POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print (form.errors)
    else:
        form =CategoryForm()
    return render(request,"rango/add_category.html", {'form': form})

