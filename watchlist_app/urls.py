from django.urls import path
from .views import movie_detail, movie_list

urlpatterns = [
    path('list/',movie_list,name='movie_list'),
    path('list/<int:pk>',movie_detail,name='movie_detail')
]

