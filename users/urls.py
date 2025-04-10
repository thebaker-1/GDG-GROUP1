from django.urls import path
from .views import RegisterView, LoginView, LogoutView, UserProfileView,UserUpdateView

urlpatterns = [
    path('auth/register', RegisterView.as_view(), name='register'),
    path('auth/login', LoginView.as_view(), name='login'),
    path('auth/logout', LogoutView.as_view(), name='logout'),
    path('users/<int:user_id>', UserProfileView.as_view(), name='user-profile'),
    path('users/<int:user_id>/update', UserUpdateView.as_view(), name='user-update'),
]