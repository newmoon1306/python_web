from rest_framework import serializers
from .models import UserModel
from django.contrib.auth.hashers import make_password #criptografar senha
from django.contrib.auth import get_user_model
from rest_framework.response import Response #responsalvel para resposta quando requisitamos
from rest_framework_simplejwt.tokens import RefreshToken #quando o token vence ele renova
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import AuthenticationFailed
class CustomTokenObtainParirSerializer(TokenObtainPairSerializer): #customizar o token quando o usuario fazer o login 
    @classmethod
    def get_token(cls, user):
        if user.suspenso:
            raise AuthenticationFailed("Conta suspensa")
        token=super().get_token(user)
        token['user_id'] = str(user.id)
        token['username'] = user.username
        token['email'] = user.email
        token['tipo'] = user.tipo
        token['suspenso'] = user.suspenso
        return token
    
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=True) #o campo tem ques ser usado pelo comando write_only
    token = serializers.SerializerMethodField() 
    class Meta:
        model=UserModel
        fields=[
            'id','username','email','password','tipo','suspenso','token'
            ]
    def get_token(self,user):
        refresh = RefreshToken.for_user(user)
        refresh['user_id'] = str(user.id)
        refresh['username'] = user.username
        refresh['email'] = user.email
        refresh['tipo'] = user.tipo
        refresh['suspenso'] = user.suspenso
        
        
    def create(self,validated_data): #garanto que o usuario vai ser criado
        validated_data['tipo'] = 'client'
        validated_data['password']=make_password(validated_data.get("password"))
        user = super().create(validated_data)
        user.token = self.get_token(user)
        return user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = [
            "id", 'username','email','tipo','suspenso'
        ]

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = [
             'username','email','password'
        ]
    username=serializers.CharField(required=False)
    email=serializers.EmailField(required=False)
    password=serializers.CharField(required=False)

