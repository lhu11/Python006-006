from django.urls import path
from . import views

urlpatterns = [
    path('index', views.books_short),
    path('star',views.books_short_star),
    path('search',views.books_search)
]