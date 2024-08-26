"""
URL configuration for IPL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin # type: ignore

from django.urls import path # type: ignore

from CSK.views import *
from RCB.views import *
from MI.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Dhoni/', Dhoni, name='Dhoni'),
    path('raina/', raina, name='raina'),
    path('virat/', virat, name='virat'),
    path('rohit/', rohit, name='rohit'),
    path('abd/', abd, name='abd'),
]
