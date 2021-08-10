from os import name
from django.urls import path
from django.views.generic import TemplateView
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',TemplateView.as_view(template_name='about.html'), name='about'),
    path('terms/',TemplateView.as_view(template_name='tnc.html'),name='tnc'),
    
    path('article/add',views.article_add, name="article_add"),
    path('article/view',views.article_view, name="article_view"),
    path('article/detail/<int:id>/',views.article_detail, name="article_detail"),
    path('article/delete/<int:id>/',views.article_delete, name="article_delete"),
    path('article/edit/<int:id>/',views.article_edit, name="article_edit"),
    
    path('currency/view',views.currency_view,name='currency_view'),
    path('contact/',views.contact,name='contact'),
    path('search/',views.search_article,name="search"),
]