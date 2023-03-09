from rest_framework import serializers
from api.models import post
from django.contrib.auth.models import User

class postserializer(serializers.ModelSerializer):
   id=serializers.CharField(read_only=True)
   description=serializers.CharField(read_only=True)
   User=serializers.CharField(read_only=True)
   data=serializers.DateField(read_only=True)

   class meta:
      model=post
      field="_all_"

class UserSerilizer(serializers.ModelSerializer):
   id=serializers.CharField(read_only=True)
   class meta:
      model=User
      field=["username","password","email","first_name","last_name"]