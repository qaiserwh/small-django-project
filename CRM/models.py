from django.db import models

# Create your models here.
class Accused(models.Model):
    name_accused=models.CharField(max_length=50)
    photo_accused=models.ImageField(upload_to='photos')
    felony_accused=models.CharField(max_length=50)
    age_accused=models.IntegerField()
    condemnation_accused=models.IntegerField()
    address_accused=models.CharField(max_length=50)
    def __str__(Self):
        return Self. name_accused


class Employe(models.Model):
    name_employee=models.CharField(max_length=50)
    photo_employee=models.ImageField(upload_to='photos')
    job_name=models.CharField(max_length=50)
    age_employees=models.IntegerField()
    Salary_employees=models.IntegerField()
    address_employees=models.CharField(max_length=50)
    def __str__(Self):
        return Self.name_employee

class FrontManager(models.Model):
    title=models.CharField(max_length=50)
    write=models.TextField()
    photo_index=models.ImageField(upload_to='photos',null=True,blank=True)
    def __str__(Self):
        return Self.title