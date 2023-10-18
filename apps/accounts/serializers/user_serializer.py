from rest_framework import serializers
from ..models.user_model import User

class UserInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('id','username','email','password')    

class UserOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('id','username','date_joined')    