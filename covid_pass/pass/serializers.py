from rest_framework import serializers
from .models import Pass


class PassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pass
        fields = ('name','age','id_number','address','status','created_at','updated_at')

