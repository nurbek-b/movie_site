from django.urls import path
from .views import *

urlpatterns = [
    path('', MoviesView.as_view(), name='movie_list'),
    path('filter/', FilterMovieView.as_view(), name='filter'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review'),
    path('actor/<str:slug>/', ActorView.as_view(), name='actor_detail'),
]