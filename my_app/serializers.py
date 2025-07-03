from rest_framework import serializers
from .models import User

class UsernameSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = '__all__'