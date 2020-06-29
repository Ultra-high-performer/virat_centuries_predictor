
from django.urls import path , include
from input_form import views

urlpatterns = [
    path('', views.home_page , name = 'home_page'),
]
