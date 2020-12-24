from account.models import DummyUser
from rest_framework import serializers


class DummyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DummyUser
        fields = ['id', 'name']
