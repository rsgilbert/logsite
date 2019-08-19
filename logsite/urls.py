from django.contrib import admin
from django.urls import path, include


app_name = 'logsite'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include(account.urls)),
    

]
