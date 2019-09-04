from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="blog_home"),
    path('/new', views.new, name='post_new'),
    path('/<int:pk>/edit/', views.post_edit, name='post_edit'),
]