from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.club, name='club'),
    path('CodingClub/', views.coding_club, name='coding_club'),
    path('RoboticsClub', views.robotics_club, name='robotics_club'),
    path('Montage', views.montage, name='montage'),
]
