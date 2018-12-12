from django.conf.urls import patterns, url
from .views.index import index
from .views.about import about
from .views.category import category
from .views.outra_view import outra_view
from .views.add_category import add_category
from .views.add_page import add_page

urlpatterns = patterns('',
        url(r'^$', index, name='index'),
        url(r'^about/$', about, name='about'),
        url(r'outra_view/',outra_view, name = 'outra_view'),
        url(r'add_category/',add_category, name ='add_category'),
        url(r'add_page/',add_page, name ='add_page'),
        url(r'^category/(?P<category_name_url>[\w\-]+)/$',category, name = 'category')
        )