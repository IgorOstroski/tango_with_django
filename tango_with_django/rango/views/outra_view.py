from django.shortcuts import render

def outra_view(request):
    dic = {'text':"Show"}
    return render(request,'rango/about.html',dic)