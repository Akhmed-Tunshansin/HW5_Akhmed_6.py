from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=20)
    duration = models.PositiveIntegerField()
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    mentor = models.ForeignKey('Mentor', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=20)
    birthdate = models.DateField()

    def __str__(self):
        return self.name


class Mentor(models.Model):
    name = models.CharField(max_length=20)
    experience = models.PositiveIntegerField()

    def __str__(self):
        return self.name
