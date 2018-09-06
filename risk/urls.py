from django.urls import path
from risk import views

urlpatterns = [
    path('',views.index,name="index"),
]