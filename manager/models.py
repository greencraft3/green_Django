from django.db import models

class BusinessCode(models.Model):
    managercode = models.CharField(max_length=20, unique=True, primary_key=True)  # 사업자코드를 기본 키로 지정
    address = models.CharField(max_length=100)  # 주소
    gasoline_price = models.IntegerField()  # 휘발유 가격
    phone_number = models.CharField(max_length=15)  # 전화번호
    pump_number = models.IntegerField()  # 주유기 번호

    def get_gasoline_price(self):
        return self.gasoline_price

    def __str__(self):
        return self.managercode

