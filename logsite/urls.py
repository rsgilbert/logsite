from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('logs/', include('logs.urls')),
    path('account/', include('account.urls')),
    path('', include('dashboard.urls')),
    path('admin/', admin.site.urls),
]




