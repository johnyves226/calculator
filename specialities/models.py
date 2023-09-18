from django.db import models


class Specialities(models.Model):
    Speciality = models.CharField(max_length=400, null=False);
    Specialities = models.CharField(max_length=400, null=False);
    Nnpoa = models.IntegerField(null=True, blank=True);
    NC = models.IntegerField(null=True, blank=True);
    CF = models.FloatField(null=True, blank=True);
    Tlcnumber = models.IntegerField(null=True, blank=True);
    Tlcf = models.FloatField(null=True, blank=True);
    HvfNumber = models.IntegerField(null=True, blank=True);
    Hvf = models.FloatField(null=True, blank=True);
    HvfAvrage = models.FloatField(null=True, blank=True);

    def __str__(self):
        return self.Speciality
