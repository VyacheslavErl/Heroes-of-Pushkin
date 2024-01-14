from django.urls import path
from . import views

urlpatterns = [
    path('', views.heroes),
    path('<int:id>', views.hero_detail),
]