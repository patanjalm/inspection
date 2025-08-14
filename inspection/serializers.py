from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "mobile_no", "full_name", "user_type", "password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
