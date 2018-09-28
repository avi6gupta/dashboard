from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.rest, name='rest'),
    path('subway/submit_subway/', views.submit_subway, name='submit'),
    path('subway/', views.subway, name='subway'),
    path('subway_check/', views.subway_check),
]
