from django.shortcuts import render
from ..forms.page import PageForm
from ..views.index import index
def add_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print (form.errors)
    else:
        form = PageForm()
    return render(request,"rango/add_page.html", {"form": form})