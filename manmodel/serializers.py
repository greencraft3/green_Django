from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import manmodel

User = get_user_model()

class ManModelSerializer(serializers.ModelSerializer):
    username = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = manmodel
        fields = ['id', 'username', 'managercode', 'total_gas', 'total_carbon', 'start_date', 'end_date']
