from django.urls import path

from redditintegration import views


urlpatterns = [
    path('oauth', views.oauth),
    path('action', views.action)
]