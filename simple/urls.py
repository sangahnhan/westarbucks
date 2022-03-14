from django.urls import path
from simple.views import ProductsView
urlpatterns = [
    path('',ProductsView.as_view()),
]
