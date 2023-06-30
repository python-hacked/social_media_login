# accounts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('login/', views.login_view, name='login'),  # Updated URL pattern name
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('socialaccount_login/<str:provider>/', views.socialaccount_login, name='socialaccount_login'),

    # ... other URLs
]
