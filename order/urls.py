from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.rest, name='rest'),
    # path('Subway/subway_submit/', views.subway_submit),
    # path('Subway/', views.subway),
    # path('subway_check/', views.subway_check),
    # path('Florentine/fw_submit/', views.fw_submit),
    # path('Florentine/', views.fw),
    # path('fw_check/', views.fw_check),
    # path('Baskin-Robbins/bnr_submit/', views.bnr_submit),
    # path('Baskin-Robbins/', views.bnr),
    # path('bnr_check/', views.bnr_check),
    path('<slug:foo>/', views.name),
    path('<slug:foo>/submit/', views.submit),
    path('<slug:foo>/check/', views.check)
]
