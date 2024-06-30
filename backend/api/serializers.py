"""Сериалайзеры для api."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели задач."""

    class Meta:
        """Мета."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
