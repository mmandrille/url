from django.urls import path
#Import Personales
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:link_id>', views.hunt_usuario, name='hunt_usuario'),
]