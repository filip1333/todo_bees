from rest_framework import serializers

from ToDoBeesBzzz.models import ToDoList


class ToDoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDoList
        fields = ('id', 'completed', 'task', 'due_date')

    def create(self, validated_data):
        return ToDoList.objects.create(**validated_data)
