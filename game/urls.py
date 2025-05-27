# game/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('mainframe/', views.mainframe, name='mainframe'),
    path('den/', views.dialtone_den, name='dialtone_den'),
    path('register/', views.register, name='register'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path("stats/", views.player_stats, name="player_stats"),
    path("explore/", views.explore, name="explore"),  # ✅ this is key
]
