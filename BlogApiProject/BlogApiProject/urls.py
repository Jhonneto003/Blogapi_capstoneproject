"""
URL configuration for BlogApiProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogapi/',include("BlogService.urls")),
    path('blogapi/',include("UserService.urls")),

    #to create a new user use this link   /api/auth/users/ -----> Post request
    #to create a token-login , use        /api/auth/token/login ------> Post request
    #to get the user details, use         /api/auth/users/ ------> Get request
    #to get authenticated user, use      /blohapi/users/profile

    path('blogapi/auth/',include('djoser.urls')),
    path('blogapi/auth/',include('djoser.urls.authtoken')),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
