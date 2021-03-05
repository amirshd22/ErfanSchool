from django.db import models

# Create your models here.
class RegisterStudent(models.Model):
    studentImage = models.ImageField(upload_to="students/", null =True , blank=True)
    grade = models.CharField(max_length=100)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    fathersName = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=13)
    studentId = models.IntegerField()

    def __str__(self):
        name = self.firstName + " " + self.lastName
        return name
    