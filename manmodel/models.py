from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from manager.models import BusinessCode
from raspi.models import ImageWithText
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta

class manmodel(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    managercode = models.ForeignKey(BusinessCode, on_delete=models.CASCADE, null=True)
    bunho = models.ForeignKey(ImageWithText, on_delete=models.CASCADE, null=True)
    total_gas = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_carbon = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    start_date = models.DateField(null=True, blank=True)  # 사용자 입력 기간 시작 날짜
    end_date = models.DateField(null=True, blank=True)  # 사용자 입력 기간 종료 날짜

    def calculate_totals(self, start_date, end_date):
        # 'end_date'의 시간을 하루의 마지막 시간으로 설정합니다.
        end_date = end_date + timedelta(days=1) - timedelta(seconds=1)

        queryset = ImageWithText.objects.filter(
            date__range=[start_date, end_date],
            managercode=self.managercode
        )
        total_gas = queryset.aggregate(Sum('fuel_consumed'))['fuel_consumed__sum'] or 0
        total_carbon = queryset.aggregate(Sum('carbon_tax'))['carbon_tax__sum'] or 0
        return total_gas, total_carbon

    def save(self, *args, **kwargs):
        # 'start_date'와 'end_date'가 인자로 전달되지 않았을 경우 기본값을 설정합니다.
        start_date = self.start_date if self.start_date else timezone.now().replace(day=1)
        end_date = self.end_date if self.end_date else timezone.now()

        # 'start_date'와 'end_date'를 사용하여 합계를 계산합니다.
        self.total_gas, self.total_carbon = self.calculate_totals(start_date, end_date)

        # 부모 클래스의 'save' 메서드를 호출하여 모델을 저장합니다.
        super().save(*args, **kwargs)
