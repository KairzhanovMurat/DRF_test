from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.ProfileApi.as_view(),name='ProfileApi')
]