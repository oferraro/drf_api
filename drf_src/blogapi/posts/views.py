# posts/views.py
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

@method_decorator(csrf_exempt, name='post')
def AddPost(request):
    payload = json.loads(request.body.decode("utf-8"))
    post = Post.objects.create(
        title=payload["title"],
        content=payload["content"]
    )
    serializer = PostSerializer(post)
    # return HttpResponse(json.dumps(serializer), content_type="application/json")
    return HttpResponse(json.dumps(serializer.data), content_type="application/json")
