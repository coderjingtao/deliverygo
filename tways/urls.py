"""tways URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,re_path, include
from comment import views
urlpatterns = [
    path('',views.index),
    path('index/',views.index),
    path('rules/',views.getNewsList),
    path('ruledetail/<int:no>',views.getNewsDetail),
    path('cityrisk',views.cityRiskAll),
    path('searchCity/',views.cityRiskByName),
    path('block/',views.roadblock),
    path('admin/', admin.site.urls),
    path('risk/',include('risk.urls')),
    path('cityall',views.show_allcity),
    path('city/<int:id>',views.show_suburbs),
    path('vote/',views.safetyVote),
    path('good/<int:id>',views.make_comment),
    path('bad/<int:id>',views.make_comment),
    path('about/',views.about),
    path('team/',views.team),
    path('showstar/',views.starry),
    path('searchstar/',views.starry),
    path('testd2/',views.d3),
    path('testd3/',views.d3),
    #re_path(r'^',views.index),
]
