"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path,re_path
from . import views
urlpatterns = [
    path('', views.index),
    path('search/<str:keyword>/<int:page>/',views.search),
    path('date/<int:year>-<int:month>-<int:day>/',views.date),
    path('redirect/<path:url>/',views.redirect),
    path('article/<int:id>/<slug:title>/',views.show_acticle)
]
