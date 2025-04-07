# Para definir las urls de la app core

from django.urls import path

from .views import home, about_us, login, register, contact

app_name = 'core'  # Nombre del namespace de la app blog

urlpatterns = [
    path("", home, name="home"),  # Vista de la página de inicio
    path("sobre-nosotros/", about_us, name="about_us"),
    path("registro/", register, name="register"),
    path("login/", login, name="login"),
    path("contacta-con-nosotros/", contact, name="contact"),
]