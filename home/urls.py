from django.contrib import admin
from django.urls import path
from  home import views

urlpatterns = [
    
   path('', views.index, name='index'),
    path('analyze', views.analysis, name='analyze'),
    path('contact',views.contact,name="contact"),
    path('about', views.about, name='about')
]
