from django.urls import path
from post import views

urlpatterns = [
    path('', views.index, name='index'),
    path('author/<int:id>', views.author, name='author'),
    path('category/<int:id>', views.category, name='category'),
    path('post/<int:id>', views.post, name='post'),
    path('add/', views.add_post, name='add'),
]