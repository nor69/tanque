from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_principal.urls')),
    path('estadisticas/', include('estadisticas.urls')),
    path('repeticiones/', include('repeticiones.urls')),
]
