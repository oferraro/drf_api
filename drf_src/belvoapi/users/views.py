from rest_framework import generics
from rest_framework.exceptions import ParseError
from .models import User
from .serializers import UserSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@method_decorator(csrf_exempt, name='balance')
def UserBalance(request):
    return HttpResponse(json.dumps({"test": "data"}), content_type="application/json")

@method_decorator(csrf_exempt, name='user')
def AddUser(request):
    payload = json.loads(request.body.decode("utf-8"))
    user = User.objects.create(
        name=payload["name"],
        email=payload["email"],
        age=payload["age"],
    )
    serializer = UserSerializer(user)
    return HttpResponse(json.dumps(serializer.data), content_type="application/json")
