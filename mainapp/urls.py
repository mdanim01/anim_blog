from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name="home"),
    path('services/<int:pk>/',views.services,name="service"),
]