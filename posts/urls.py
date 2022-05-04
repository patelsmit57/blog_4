from unicodedata import name
import django


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.all_blog, name='all_blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('favorite/', views.favorite),
    path('read_leter/', views.read_later, name='read_later'),
]
