from django.urls import path
from . import views

urlpatterns = [
    path("", views.homePage  , name='home'),
    path('Blogs/', views.BlogPage , name='Blog'),
    path('blog/<int:blog_id>/', views.blogDetails , name='details')
]
