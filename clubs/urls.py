from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.club, name='club'),
    path('<slug:foo>/', views.club_type, name='club_type'),
    # path('RoboticsClub', views.robotics_club, name.html='robotics_club'),
    # path('Montage', views.montage, name.html='montage'),
    path('<slug:foo>/add', views.add, name='add')
]
