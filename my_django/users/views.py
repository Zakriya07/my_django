from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from base.success import SuccessResponse

from .serializers import *

# Create your views here.

class SignUP(APIView):
    def post(self,request):
        if request.data.get('role') == None :
            return Response(data={'message':'Role field is missing'},status=status.HTTP_400_BAD_REQUEST)
        if request.data.get('role') == 1 :
            serializer=TeacherSerializer(request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return SuccessResponse(serializer.data)
        if request.data.get('role') == 2 :
            serializer=StudentSerializer(request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return SuccessResponse(serializer.data)
        if request.data.get('role') == 3 :
            serializer=ParentSerializer(request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return SuccessResponse(serializer.data)
            
            

