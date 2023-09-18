from django.db import models


class Speciality(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Object(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    phone_number2 = models.CharField(max_length=20)
    speciality = models.ForeignKey('Speciality', related_name="specialities", on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    services = models.ForeignKey('Service', related_name="service", on_delete=models.CASCADE)
    demande_object = models.ForeignKey('Object', related_name="object", on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + self.last_name
