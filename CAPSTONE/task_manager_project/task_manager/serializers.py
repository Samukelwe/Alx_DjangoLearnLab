from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task  
from datetime import date

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])  
        user.save()
        return user
    
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'  
        read_only_fields = ['user', 'completed_at']  

    def validate_due_date(self, value): 
        if value < date.today():
            raise serializers.ValidationError("Due date must be in the future.")
        return value