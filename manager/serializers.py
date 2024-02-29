from rest_framework import serializers
from .models import BusinessCode

class BusinessCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessCode
        fields = ['managercode', 'address', 'gasoline_price', 'phone_number', 'pump_number']
