# yourapp/serializers.py

from rest_framework import serializers
from .models import ImageWithText

class ImageWithTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageWithText
        fields = ('id', 'car_img', 'car_class', 'bunho_img', 'bunho_text', 'bunho_class', 'date',
                  'carcode', 'managercode', 'refuel_amount', 'fuel_consumed', 'carbon_tax')
