"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from calendarNote import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('order/', include('order.urls')),
    path('calendar', views.CalendarListView.as_view(), name='calendar'),
    path('entry/<int:pk>', views.EntryDetailView.as_view(), name='details'),
    path('entry/add', views.add, name='add'),
    path('entry/delete/<int:pk>', views.delete, name='delete'),
    path('admin/', admin.site.urls),
    path('clubs/', include('clubs.urls')),
    path('signup/', include('accounts.urls')),
    path('change/', include('accounts.urls')),
    path('', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

