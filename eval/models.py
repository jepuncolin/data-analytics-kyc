from django.db import models

# Create your models here.
class KYC(models.Model):
    com_id=models.IntegerField()
    amt=models.DecimalField(max_digits=20,decimal_places=6)
    ano=models.CharField(max_length=10)
