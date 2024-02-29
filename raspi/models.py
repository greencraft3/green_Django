from django.db import models
from car.models import Car

from manager.models import BusinessCode


class ImageWithText(models.Model):
    id = models.BigAutoField(primary_key=True)
    carcode = models.ForeignKey(Car, on_delete=models.CASCADE)
    managercode = models.ForeignKey(BusinessCode, on_delete=models.CASCADE)
    car_img = models.ImageField(upload_to='captured_images/')
    car_class = models.TextField()
    bunho_img = models.ImageField(upload_to='captured_images/')
    bunho_text = models.TextField()
    bunho_class = models.TextField()
    refuel_amount = models.IntegerField()  # 주유한 금액 (정수)
    fuel_consumed = models.DecimalField(max_digits=10, decimal_places=2)  # 주유된 휘발유 (소수점 둘째 자리까지)
    carbon_tax = models.DecimalField(max_digits=10, decimal_places=2)  # 탄소세 (소수점 둘째 자리까지)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def get_carbon_tax(self):
        try:
            car_instance = Car.objects.get(name=self.carcode.name)
            return car_instance.carbon_tax
        except Car.DoesNotExist:
            return None

    def get_gasoline_price(self):
        try:
            business_code_instance = BusinessCode.objects.get(managercode=self.managercode)
            return business_code_instance.gasoline_price
        except BusinessCode.DoesNotExist:
            return None