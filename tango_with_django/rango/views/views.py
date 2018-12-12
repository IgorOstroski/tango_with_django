from django.shortcuts import render
#from django.http import HttpResponse
from .models.category import Category
from .models.page import Page
from .forms.category import CategoryForm
from .forms.page import PageForm

def index(request):
    category_list = Category.objects.order_by('-views')[:5]
    context_dic = {'categories': category_list}
    return render(request,'rango/index.html',context_dic)

def about(request):
    context_dic = {'text': "Testando..."}
    return render(request,'rango/about.html',context_dic)

def outra_view(request):
    dic = {'text':"Show"}
    return render(request,'rango/about.html',dic)

def category(request,category_name_url):
    context_dic = {}
    try:
        category = Category.objects.get(slug=category_name_url)
        context_dic['category_name'] = category.name
        pages = Page.objects.filter(category=category)
        context_dic['pages'] = pages
        context_dic['category'] = category

    except Category.DoesNotExist:
        pass

    return render(request,'rango/category.html',context_dic)


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