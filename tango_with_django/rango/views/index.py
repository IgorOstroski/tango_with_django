from django.shortcuts import render
from ..models.category import Category

def index(request):
    category_list = Category.objects.order_by('-views')[:5]
    context_dic = {'categories': category_list}
    return render(request,'rango/index.html',context_dic)
