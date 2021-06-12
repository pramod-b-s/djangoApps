from . import views
from django.urls import path

app_name = "blog"
urlpatterns = [
    path('', views.PostsIndexView.as_view(), name='home'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
]