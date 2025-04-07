"""
URL configuration for firstpage_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # Importo include para incluir las urls de las apps

urlpatterns = [
    path("", include("core.urls", namespace="core")),  # Incluyo las urls de app
    path("blog/", include("blog.urls", namespace="blog")),
    path("cursos/", include("courses.urls", namespace="courses")),
    path('admin/', admin.site.urls),
]
