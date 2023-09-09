from rest_framework import serializers
from .models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email','first_name','last_name')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class GetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
class AllergySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Allergies
        fields = '__all__'
        
class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model  = HealthIssue
        fields = '__all__'