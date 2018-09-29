from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.rest, name='rest'),
    path('Subway/submit/', views.submit),
    path('Subway/', views.subway),
    path('subway_check/', views.subway_check),
    path('Florentine/submit/', views.submit),
    path('Florentine/', views.fw),
    path('fw_check/', views.fw_check),
    path('Baskin-Robbins/submit/', views.submit),
    path('Baskin-Robbins/', views.bnr),
    path('bnr_check/', views.bnr_check),
]
