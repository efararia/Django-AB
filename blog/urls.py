from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_view, name='index'),
    path('<int:pid>/', views.blog_single, name='single'),
]
