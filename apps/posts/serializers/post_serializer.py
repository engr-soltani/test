from rest_framework import serializers

from ...accounts.models.user_model import User
from ..models.post_model import Post

class PostInputSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.all())
  
    def create(self, validated_data):

        post_instance = Post.objects.create(**validated_data)
        return post_instance
    
    class Meta:
        model = Post
        fields ='__all__'

class PostOutputSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.all())
    class Meta:
        model = Post
        fields ='__all__'