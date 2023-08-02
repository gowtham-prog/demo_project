from .models import Project,User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class RegisterSerializer (serializers.ModelSerializer):
    username = serializers.CharField(required = True,validators = [UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(required = True ,validators  = [UniqueValidator(queryset = User.objects.all())])
    password  = serializers.CharField(required = True, write_only = True ,validators = [validate_password] )
    confirmation = serializers.CharField(required = True, write_only = True)
    class Meta :
        model = User
        fields = ('username','email','password','confirmation')
    def validate(self,attrs):
        if attrs['password'] != attrs['confirmation'] :
            raise serializers.ValidationError({"password" : "passwords didn't match"})
        return attrs
    
    def create(self,validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email']
        )
        user.set_password(validated_data["password"])
        user.save()
        return user