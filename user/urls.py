from django.urls import path
from user import views

urlpatterns = [
    path('sign-up/', views.signup, name='sign-up'),
    path('sign-in', views.signin, name='sign-in'),
    path('logout/', views.Logout, name='logout'),
]