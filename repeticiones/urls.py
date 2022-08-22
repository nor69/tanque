from django.urls import path
from . import views

urlpatterns = [
    path('', views.repeticiones, name="Repeticiones"),
    path('<int:paso_id>', views.video, name="Video"),
]
