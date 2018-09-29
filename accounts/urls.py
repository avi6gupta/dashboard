from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.signup, name='signup'),
    path('signup_add/', views.signup_add, name="signup_add"),
    path('secy_change/', views.secy_change, name="secy_change"),
    path('secy_changed/', views.secy_changed, name="secy_changed"),
]
