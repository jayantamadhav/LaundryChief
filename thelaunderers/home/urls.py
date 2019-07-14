from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('../dashboard/', include('dashboard.urls')),
    path('auth/signup', views.signup, name='signup'),
]