from blog import views
from django.urls import path

# blog/
urlpatterns = [
    path('', views.blog, name= 'blog'),
    path('exemplo/', views.exemplo, name= 'exemplo'),
]