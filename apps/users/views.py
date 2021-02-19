from django.conf import settings
from django.utils.translation import ugettext as _
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.tokens import RefreshToken

# from django_filters import rest_framework as filters

from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.views import Response, status, APIView
from rest_framework.decorators import api_view
from rest_framework import exceptions
# from rest_framework import filters as df

from . import serializers


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializers.MyTokenObtainPairSerializer



class RegisterView(CreateAPIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = serializers.UserCreateSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.email = user.email.lower()
        user.username = user.email
        user.is_active = True
        user.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
