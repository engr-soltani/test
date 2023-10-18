from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from social_media_project import settings

from ..models.post_model import Post
from ..serializers.post_serializer import PostInputSerializer, PostOutputSerializer

class PostView(APIView):
     
    def post(self, request):
        
        serializer = PostInputSerializer(context = {"request": request}, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):

        posts = Post.objects.all()
        serializer = PostOutputSerializer(posts,many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)