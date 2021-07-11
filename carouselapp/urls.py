from django.urls import path, include
from .import views

app_name = 'carouselapp'

urlpatterns = [
    path('',views.slider,name='slider')
]
