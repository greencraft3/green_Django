from rest_framework import viewsets
from .models import manmodel
from .serializers import ManModelSerializer
from django.utils.dateparse import parse_date

class ManModelViewSet(viewsets.ModelViewSet):
    queryset = manmodel.objects.all()
    serializer_class = ManModelSerializer
    lookup_field = 'id'

    def perform_create(self, serializer):
        # validated_data에서 날짜를 가져옵니다.
        start_date = serializer.validated_data.get('start_date')
        end_date = serializer.validated_data.get('end_date')

        # Serializer를 통해 manmodel 인스턴스를 생성합니다.
        instance = serializer.save()

        # 생성된 인스턴스를 사용하여 total_gas와 total_carbon을 계산합니다.
        total_gas, total_carbon = instance.calculate_totals(start_date, end_date)

        # 계산된 값을 인스턴스에 저장합니다.
        instance.total_gas = total_gas
        instance.total_carbon = total_carbon
        instance.save()
