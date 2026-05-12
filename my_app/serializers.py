# serializers.py

from .models import *
from rest_framework import serializers


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'id',
            'username',
            'email',
            'student_class',
            'is_active',
            'is_staff',
            'avatar'
        ]


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = Users
        fields = [
            'id',
            'username',
            'email',
            'student_class',
            'is_active',
            'is_staff',
            'avatar'
        ]

    def get_avatar(self, obj):
        try:
            if not obj.avatar:
                return None

            request = self.context.get('request')

            if request:
                return request.build_absolute_uri(obj.avatar.url)

            return obj.avatar.url

        except Exception as e:
            print("AVATAR ERROR:", str(e))
            return None 