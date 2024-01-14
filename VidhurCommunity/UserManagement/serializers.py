from rest_framework import serializers
from django.contrib.auth import get_user_model
Users = get_user_model()
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Users
        fields = ['id', 'first_name', 'last_name', 'email','phone']


class LoginSerializer(serializers.ModelSerializer):


    email = serializers.EmailField(max_length=255, min_length=3,required=True)
    password = serializers.CharField(max_length=68, min_length=4, write_only=True,required=True)
    first_name = serializers.CharField(max_length=255, min_length=6, read_only=True)
    phone = serializers.CharField(max_length=15, min_length=20, read_only=True)
    last_name = serializers.CharField(max_length=15, min_length=6, read_only=True)
    
    class Meta:
        model = Users
        fields = ['id', 'first_name', 'last_name', 'email','phone','password']

    def validate(self, attrs):


        email = attrs.get('email','')
        password = attrs.get('password','')

        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        
        result = user.get_tokens_for_user()

        return result


    
