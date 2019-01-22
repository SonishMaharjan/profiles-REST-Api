# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

from . import serializers

class HellooApiView(APIView):
    """Test Api view haha """
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Return list Api view features"""

        api_views=['uses Http methods as fxn',
            'similar to traditional django view',
            'gives more control of logic',
            'mapped manually to URLS',
        ]

        return Response({"message":"hello RestApi",
            "api_view":api_views,
                    })
    def post(self,request):
        """Create a hello message with our name"""
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "hello {0}".format(name)
            return Response({"message":message})
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk = None):
        """Handle the update of an object"""
        return Response({"method":"PUT"})

    def patch(self,request,pk=None):
        """Patch request only update the field provided in request"""
        return Response({"message":"PATCH"})
    def delete(self,request, pk =None):
        """ Delete object"""
        return Response({"method":"DELETE"})
