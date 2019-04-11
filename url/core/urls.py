from django.urls import path
#Import Personales
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('i/<int:link_id>', views.redirect_id, name='redirect_id'),
    path('n/<slug:link_nombre>', views.redirect_nombre, name='redirect_nombre'),
]