from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser
# Create your views here.

class PostListView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Post.objects.all()
    serializer_class = PostSerializer