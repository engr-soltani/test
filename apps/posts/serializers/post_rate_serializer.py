from rest_framework import serializers

from ...accounts.models.user_model import User
from ..models.post_rate_model import PostRate
from ..models.post_model import Post
from django.db.models import Count
from django.db.models import Avg

class PostRateInputSerializer(serializers.ModelSerializer):
  
    def create(self, validated_data):
        
        post_rate_list_instance = PostRate.objects.filter(post_id=validated_data['post'].pk)
        post_rate_instance = post_rate_list_instance.filter(user_id=validated_data['user']).first()

        if post_rate_instance == None:
            post_rate_instance = PostRate.objects.create(**validated_data)
        else:
            post_rate_instance.rate = validated_data['rate']
            post_rate_instance.save()

        number_rates = post_rate_list_instance.aggregate(Count('rate'))
        avg_rates = post_rate_list_instance.aggregate(Avg('rate'))
        post_instance = Post.objects.filter(id =validated_data['post'].pk).first()

        post_instance.number_rates = number_rates['rate__count']
        post_instance.avg_rates = avg_rates['rate__avg']
        post_instance.save()

        return post_rate_instance
    
    class Meta:
        model = PostRate
        fields ='__all__'