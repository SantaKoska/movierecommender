from django.urls import path
from . import views
urlpatterns = [
    path('Movierec/', views.front, name='Movierec'),
]