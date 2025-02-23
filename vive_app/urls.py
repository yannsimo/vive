from django.urls import path
from . import views  # Importer les vues de l'application

urlpatterns = [
    path('', views.home, name='home'),
    path('particulier/', views.particulier, name='particulier'),
    path('collectivite/', views.collectivite, name='collectivite'),
    path('manifeste/', views.manifeste, name='manifeste'),
    path('contact/', views.contact, name='contact'),
]
