from django.urls import path
#Import Personales
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:link_id>', views.redirect_id, name='redirect_id'),
    path('<slug:link_nombre>', views.redirect_nombre, name='redirect_nombre'),
]