from django.urls import path
from django.contrib.auth.views import LoginView
from .views import signup_view, profile_view, logout_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
]
