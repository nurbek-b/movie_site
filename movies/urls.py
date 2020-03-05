from django.urls import path
from .views import *

urlpatterns = [
    path('', MoviesView.as_view(), name='movie_list'),
    path('<slug:slug>/', MovieDetail.as_view(), name='movie_detail'),
]