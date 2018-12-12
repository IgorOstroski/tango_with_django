from django.shortcuts import render
from ..models.category import Category
from ..models.page import Page

def category(request,category_name_url):
    context_dic = {}
    try:
        category = Category.objects.get(slug=category_name_url)
        category.views = category.views + 1
        category.save()
        context_dic['category_name'] = category.name
        context_dic['category_comments'] = category.comments
        pages = Page.objects.filter(category=category)
        context_dic['pages'] = pages
        context_dic['category'] = category

    except Category.DoesNotExist:
        pass

    return render(request,'rango/category.html',context_dic)
