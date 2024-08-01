from django.urls import path

from .views import SendHttpRequest


urlpatterns = [
    path('', SendHttpRequest.as_view()),
] 
