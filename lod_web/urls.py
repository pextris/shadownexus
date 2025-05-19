from django.contrib import admin
from django.urls import path, include
from game import views

urlpatterns = [
    path('', views.index, name='home'),
    path('mainframe/', views.mainframe, name='mainframe'),
    path('den/', views.dialtone_den, name='dialtone_den'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # login/logout/password reset
]

