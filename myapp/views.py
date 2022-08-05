from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import socket

# Create your views here.
class HelloAPI(APIView):
    def get(self,request):
        h_name = socket.gethostname()
        IP_addres = socket.gethostbyname(h_name)
        print("Host Name is:" + h_name)
        print("Computer IP Address is:" + IP_addres)
        return Response({"Result":f"Hello From {IP_addres}"})