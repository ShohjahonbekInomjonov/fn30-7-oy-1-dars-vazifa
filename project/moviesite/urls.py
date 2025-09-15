from django.urls import path
from .views import main, about, add_movie, delete_movie, update_movie, by_genre, by_movie, profile, edit_profile

urlpatterns = [
    path('', main, name='main'),
    path('about/', about, name='about'),
    path('movie/add/', add_movie, name='add_movie'),
    path('movie/<int:movie_id>/delete/', delete_movie, name='delete_movie'),
    path('movie/<int:movie_id>/update/', update_movie, name='update_movie'),
    path('genre/<int:genre_id>/', by_genre, name='by_genre'),
    path('movie/<int:movie_id>/', by_movie, name='by_movie'),
    path('profile/<str:username>/', profile, name="profile"),
    path('profile/<str:username>/edit/', edit_profile, name="edit_profile"),
]
