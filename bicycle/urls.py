from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_bicycle, name='name-bike'),
    path('/<str:model>', views.get_description, name='name-model'),
]
