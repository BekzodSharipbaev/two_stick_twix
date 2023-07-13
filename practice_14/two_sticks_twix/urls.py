"""
URL configuration for two_sticks_twix project.

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
from django.urls import include, path

from right_stick.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_products),
    path('left_stick/', include('left_stick.urls', namespace='left_stick')),
    path('right_stick/', include('right_stick.urls', namespace='right_stick')),
]
