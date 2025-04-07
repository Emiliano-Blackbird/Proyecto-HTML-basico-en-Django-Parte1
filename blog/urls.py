# Para definir las urls de la app core

from django.urls import path

from .views import blog_detail, blog_list

app_name = 'blog'  # Nombre del namespace de la app blog

urlpatterns = [
    path("", blog_list, name="blog_list"),
    path("<int:id>/", blog_detail, name="blog_detail"),
]