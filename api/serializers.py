#kun model serialize garni vanera specify garni
from dataclasses import fields
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__' #which field we wanna see? so all view garna all
        