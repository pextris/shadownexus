from django.contrib import admin
from django.urls import path, include
from game import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # Direct view paths
    path("", views.index, name="home"),
    path("mainframe/", views.mainframe, name="mainframe"),
    path("den/", views.dialtone_den, name="dialtone_den"),
    path("explore/", views.explore, name="explore"),  # ✅ ADD THIS LINE
    path("register/", views.register, name="register"),
    path("accounts/login/", views.login_view, name="login"),
    path("accounts/logout/", views.logout_view, name="logout"),
    path("stats/", views.player_stats, name="player_stats"),

    # Optional: built-in auth
    path("accounts/", include("django.contrib.auth.urls")),
]
