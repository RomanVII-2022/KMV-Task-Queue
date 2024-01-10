from django.shortcuts import render
from myapp.tasks import sendEmail
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class SendEmailAPIView(APIView):
    def post(self, request, format=None):
        sendEmail.delay(request.data['email'])
        return Response(status=status.HTTP_200_OK)
