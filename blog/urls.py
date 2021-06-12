from . import views
from django.urls import path

app_name = "blog"
urlpatterns = [
    path('', views.AllPostsIndexView.as_view(), name='home'),    
    path('create/', views.post_create, name='create'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('posts/', views.AllPostsIndexView.as_view(), name='all_posts'),
]