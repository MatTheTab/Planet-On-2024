from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_home, name='search-home'),
    path('search-similar-projects/', views.search_similar_projects, name='search_similar_projects')
]
