from rest_framework import serializers
from .models import Record


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'


class RecordeditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ['name', 'description', 'email']
