from django.db import models


class Student(models.Model):
    fullnames = models.CharField(max_length=30, blank=False)
    email = models.EmailField()
    age = models.IntegerField()
    phone = models.IntegerField()
    classcode = models.CharField(max_length=30, blank=False)


    def __str__(self):
        return   f"{self.fullnames} {self.email} {self.age} {self.phone}"

class Teacher(models.Model):
    name = models.CharField(max_length=30, blank=False)
    subject = models.CharField(max_length=50,blank=False)
    tsenum = models.CharField(max_length=30,blank=False)


    def __str__(self):
        return  f"{self.name} {self.subject} {self.tsenum}"


