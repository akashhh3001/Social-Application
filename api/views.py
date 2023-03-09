from django.shortcuts import render
from rest_framework.response import Response
from api.serializer import UserSerilizer,postserializer
from api.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django.contrib.auth.models import User
from api.models import post

# class postModelView(ModelViewSet):
#    # authentication_classes=
