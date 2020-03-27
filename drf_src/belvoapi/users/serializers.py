# users/serializers.py
from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'email', 'age', 'created_at', 'updated_at',)
        model = models.User
