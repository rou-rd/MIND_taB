from rest_framework import serializers
from config.models import config


class ConfigSerializer(serializers.Serializer):
    keywords=serializers.CharField(max_length=200)
    date=serializers.DateTimeField(auto_now_add=True)
    everyday=serializers.BooleanField(default=True)
    everyweek=serializers.BooleanField(default=False)
    everymonth=serializers.BooleanField(default=False)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)
