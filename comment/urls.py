from django.urls import path
from comment import views

urlpatterns = [
    path('cityall',views.show_allcity),
    path('city/<int:id>',views.show_suburbs),
]