from django.urls import path
from .views import ListCloths,DetailView
from . import views

urlpatterns = [
    path('cloths/',ListCloths.as_view(),name='cloths'),
    path('details/<int:pk>/',DetailView.as_view(),name = 'details')
]