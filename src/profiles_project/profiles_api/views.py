# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
#for login api
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

#if not authenticated read only can be done
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#must be authenitcated to read too
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from . import permissions
from . import models

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



class HelloViewSet(viewsets.ViewSet):
    """ Test api view set"""
    serializer_class = serializers.HelloSerializer
    def list(self,request):
        """ Return a hello message"""
        a_viewset = ["Uses action (list, create, retrieve, update, partialupdate,"
                    "destroy)",
                    "Automatically maps to URLs using router",
                    "Provides more functionality wiht less code",]
        return Response({"message":"Hello from viewset",
                        "a_viewset": a_viewset
                        })

    def create(self,request):
        """Create a new hello message"""
        serializer = serializers.HelloSerializer(data = request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello new {0}".format(name)
            return Response({"message":message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk= None):
        """Handle getting object by ID"""
        return Response({"http_method":'GET'})
    def update(self,request,pk=None):
        """Handle all the editing of object by ID"""
        return Response({"http_method":"POST"})
    def partial_update(self,request,pk=None):
        """Handle all the partial update. Correspond to http PATCH method"""
        return Response({"http_method":"PATCH"})

    def destroy(self,request,pk=None):
        """Delet the object of given key"""
        return Response({"http_method": "DELETE"})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles createing , updating retrieving profiles"""
    serializer_class = serializers.UserProfileSerializer
    #says how to retrieve object from data Base
    #list all the object from the data Base
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    #adding search for backends
    filter_backends = (filters.SearchFilter,)
    search_fields =("name","email",)

class LoginViewSet(viewsets.ViewSet):
    """Checks email and passwork and return an auth token"""
    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token"""
        return ObtainAuthToken().post(request)

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handle creating,reading and updating profile feed item"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer

    queryset= models.ProfileFeedItem.objects.all()
    #IsAuthenticatedOrReadOnly is changed into IsAuthenticated
    #now user have authenticated before reading data too
    permission_classes = (permissions.PostOwnStatus,IsAuthenticated)
    #when django object create new view set it will Run
    #genrally used to customize-- here user who created feed is equals to current user
    def perform_create(self,serializer):
        """sets user profile to login user"""
        serializer.save(user_profile= self.request.user)
