from django.contrib import admin
from django.urls import path, include
from . import views
from ticket.views import *
from django.views.generic import TemplateView


urlpatterns = [
   
    path('', views.cont_list, name='index'),
   
    

    path('about/', ShcontView.as_view(template_name="about.html")),
    
    path('catalog/', CatalogView.as_view(template_name="catalog.html")),
    path('catalog/<slug>/', CatalogClassView.as_view(), name='catalogclassview'),
    path('catalog/category/<slug>/', CatalogVidView.as_view(), name='catalogvidview'),
    path('catalog/3/<slug>/', CatalogDuView.as_view(), name='du'),
    path('catalog/q/<slug>/', SelectPrice.as_view(), name='selectprice'),

    path('contact/', TemplateView.as_view(template_name="contact.html")),
    path('obrsvaz/add/', views.tag_form_redirect, name="obrsvaz1.html"),
    path('obrsvaz/', TagCreate.as_view(), name='tag_create_url'),
    path('poleznoe/', TemplateView.as_view(template_name="poleznoe.html")),
    path('uslugi/', ServiceView.as_view(template_name="uslugi.html")),
    path('works/', TemplateView.as_view(template_name="works.html")),


    ]