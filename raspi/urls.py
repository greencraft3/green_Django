from django.urls import path
from .views import ImageWithTextListView
from .views import GetCarTaxView
from .views import GetGasolinpriceView
urlpatterns = [
    path('image-with-text/', ImageWithTextListView.as_view(), name='image-with-text'),
    # Add other URLs if needed
    path('get_car_tax/', GetCarTaxView.as_view(), name='get_car_tax'),
    path('get_gasoline_price/', GetGasolinpriceView.as_view(), name='get_gasoline_price')
]
