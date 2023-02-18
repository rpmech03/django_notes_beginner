from django.db import models
class Emp(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    address=models.CharField(max_length=20)
    sal=models.IntegerField()
    def __str__(self) -> str:
        return self.name
