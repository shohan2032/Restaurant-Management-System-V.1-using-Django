"""projectHub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import django
from django.contrib import admin
from django.urls import path,include
from django.conf import settings##for images which is in our db and also in static --> images file
from django.conf.urls.static import static##for images which is in our db and also in static --> images file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ownerpanel/',include('Owner_Panel.urls')),
    # path('ownerlogin/',include('django.contrib.auth.urls')),
    # path('ownerlogin/',include('ownerlogin.urls')),
    # path('',include('ownerlogin.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)