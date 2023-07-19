from django.urls import path
from .views import ListCloths, DetailView, AddToCartView
from . import views

urlpatterns = [
    path('cloths/',ListCloths.as_view(),name='cloths'),
    path('details/<int:pk>/',DetailView.as_view(),name = 'details'),
    path('add-to-cart/', AddToCartView.as_view(), name='add-to-cart'),
]