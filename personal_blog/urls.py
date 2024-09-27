from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls")),
    path('games/<str:game_name>/', views.game_detail, name='game_detail'),
    path('games/<int:game_id>/', views.game_detail, name='game_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
