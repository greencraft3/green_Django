
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import ImageWithText
from .serializers import ImageWithTextSerializer
from car.models import Car
from manager.models import BusinessCode


class ImageWithTextListView(generics.ListCreateAPIView):
    queryset = ImageWithText.objects.all()
    serializer_class = ImageWithTextSerializer
    lookup_field = 'id'
class GetCarTaxView(APIView):
    def get(self, request, *args, **kwargs):
        class_label = request.GET.get('image_id')

        try:
            car_instance = Car.objects.get(id=class_label)
            carbon_tax = car_instance.get_carbon_tax()

            if carbon_tax is not None:
                return Response({'carbon_tax': carbon_tax})
            else:
                return Response({'error': 'Car not found'}, status=status.HTTP_404_NOT_FOUND)
        except ImageWithText.DoesNotExist:
            return Response({'error': 'Image not found'}, status=status.HTTP_404_NOT_FOUND)


class GetGasolinpriceView(APIView):
    def get(self, request, *args, **kwargs):
        managercode = request.GET.get('managercode')

        try:
            business_code_instance = BusinessCode.objects.get(managercode=managercode)
            gasoline_price = business_code_instance.get_gasoline_price()

            if gasoline_price is not None:
                return Response({'gasoline_price': gasoline_price})
            else:
                return Response({'error': 'Gasoline price not found'}, status=status.HTTP_404_NOT_FOUND)
        except BusinessCode.DoesNotExist:
            return Response({'error': 'BusinessCode not found'}, status=status.HTTP_404_NOT_FOUND)
