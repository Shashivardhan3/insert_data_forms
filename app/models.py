from django.db import models

# Create your models here.

class school(models.Model):
    SCName=models.CharField(max_length=100,default=True)
    SCPrincipal=models.CharField(max_length=100)
    SClocation=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.SCName
    


class student(models.Model):
    SCName=models.ForeignKey(school,on_delete=models.CASCADE)
    SName=models.CharField(max_length=100)
    Sid=models.IntegerField(primary_key=True)

    def __str__(self) -> str:
        return self.SName


