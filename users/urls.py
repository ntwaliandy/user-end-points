from unicodedata import name
from django.urls import path, include
from .views import RegisterApi, LoginApi, MainUser
from knox import views as knox_views

urlpatterns = [
    path('api/register/', RegisterApi.as_view(), name='register'),
    path('api/login/', LoginApi.as_view(), name='login'),
    path('api/logout', knox_views.LogoutView.as_view(), name='logout'),
    path('api/auth/user/', MainUser.as_view()),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
