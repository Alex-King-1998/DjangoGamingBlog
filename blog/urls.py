from django.urls import path
from . import views
from .views import add_game, game_detail, games_list, contact

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
    path('games-list/', views.games_list, name='games_list'),
    path('contact/', contact, name='contact'),
    path('game/<str:game_name>/', views.game_detail, name='game_detail'), 
    path('games/add/', add_game, name='add_game'),
    path('games/<int:game_id>/', game_detail, name='game_detail'),
    path('games/', games_list, name='games_list'),
]
