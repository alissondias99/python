from blog import views
from django.urls import path

# blog/
urlpatterns = [ # define o comportamento das urls dentro de blog
    path('post/', views.blog, name= 'blog'),
    path('post/<int:post_id>', views.post, name= 'post'),
    path('exemplo/', views.exemplo, name= 'exemplo'),
]