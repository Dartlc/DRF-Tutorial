from rest_framework import serializers

from .models import SignUp
from .foreign_key import TestForeignkey


class SignupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SignUp
        fields = ['name', 'mobile_number']


class KeySerializer(serializers.ModelSerializer):
    signup_id = SignupSerializer(required=False)

    class Meta:
        model = TestForeignkey
        fields = ['signup_id']
