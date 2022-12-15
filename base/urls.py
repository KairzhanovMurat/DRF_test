from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

my_router = DefaultRouter()

my_router.register('MyViewSet', views.MyViewSet, basename='MyViewSet')
my_router.register('profile',views.UserViewSet)
urlpatterns = [
    path('api/', views.ProfileApi.as_view(), name='ProfileApi'),
    path('viewset/', include(my_router.urls))
]
