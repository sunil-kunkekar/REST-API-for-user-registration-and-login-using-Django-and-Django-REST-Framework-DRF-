# # myapp/serializers.py

# from django.contrib.auth.models import User
# from rest_framework import serializers

# class UserSerializer(serializers.Serializer):
#     class Meta:
#         model        = User
#         fields       = ['id','username','password']
#         extra_kwargs = {'password': {'write_only': True}}

#         def create (self, validated_data):
#             user = User.objects.create_user(
#                 username = validated_data['username'],
#                 password = validated_data['password']
#             )
#             return user
        


from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
