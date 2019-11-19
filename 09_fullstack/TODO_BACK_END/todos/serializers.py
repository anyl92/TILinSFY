from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    class Meta:
        model = Todo
        fields = ('id', 'title', 'completed', )
