from django.contrib import admin
from .models import ImageWithText  # 'YourManagerModel'은 관리하고자 하는 모델의 실제 이름으로 변경하세요.

admin.site.register(ImageWithText)
