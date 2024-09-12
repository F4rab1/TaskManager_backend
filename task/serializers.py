from rest_framework import serializers
from .models import Task, Category, Note, Customer
from datetime import date


class TaskSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'stage', 'priority', 'category', 'created_at', 'completion_date', 'customer', 'isFlagged']
    category = serializers.StringRelatedField()


class AddTaskSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'category', 'completion_date', 'isFlagged']

    def validate_completion_date(self, completion_date):
        if completion_date < date.today():
            raise serializers.ValidationError("The completion date cannot be in the past.")
        return completion_date


class UpdateStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['stage']  


class CategorySerilizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['title', 'text', 'created_at']


class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Customer
        fields = ['id', 'user_id', 'phone', 'birth_date']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().update(instance, validated_data)