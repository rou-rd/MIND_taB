from rest_framework import serializers
from .models import concurrent_api


class concurrent_apiSerializer(serializers.ModelSerializer):


	class meta:
		model=concurrent_api
		fields='__all__'

