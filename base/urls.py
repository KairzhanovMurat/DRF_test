from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

my_router = DefaultRouter()

my_router.register('MyViewSet', views.MyViewSet, basename='MyViewSet')
my_router.register('profile', views.UserViewSet)
my_router.register('feed', views.FeedItemView)
urlpatterns = [
    path('api/', views.ProfileApi.as_view(), name='ProfileApi'),
    path('login/', views.AuthViewApi.as_view()),
    path('viewset/', include(my_router.urls))
]
