from django.conf import settings
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=6, blank=True)
    # validators=[])를 통해서 숫자만쓰일 수 있게 유효성 검사를 할 수 있다.