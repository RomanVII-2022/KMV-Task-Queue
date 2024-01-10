from django.urls import path, include
from myapp.views import SendEmailAPIView
from rest_framework import routers

urlpatterns = [
    path('send-email', SendEmailAPIView.as_view(), name='email')
]
