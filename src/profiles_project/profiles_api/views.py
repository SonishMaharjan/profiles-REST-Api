# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HellooApiView(APIView):
    """Test Api view haha """
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
