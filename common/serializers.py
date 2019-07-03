from rest_framework import serializers

from common.models import ToDoList


class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ('task', 'due_date', 'completed')

    def create(self, validated_data):
        return ToDoList.objects.create(**validated_data)


class ToDoEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ('id', 'task', 'completed', 'due_date')


class ToDoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ('id', 'task', 'completed', 'due_date')

    def update(self, instance, validated_data):
        return ToDoList.objects.update(**validated_data)
