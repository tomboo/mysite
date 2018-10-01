from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Weight(models.Model):

    # Fields
    date = models.DateField(default=timezone.now)
    weight = models.FloatField()
    body_fat = models.FloatField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Metadata
    class Meta:
        ordering = ['user', '-date']

    # Methods
    def __str__(self):
        return f'{self.date}, {self.weight}, {self.body_fat}, {self.user}'


class BloodPressure(models.Model):

    # Fields
    date = models.DateField(default=timezone.now)
    systolic = models.IntegerField()
    diastolic = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Metadata
    class Meta:
        ordering = ['user', '-date']

    # Methods
    def __str__(self):
        return f'{self.date}, {self.systolic}/{self.diastolic}, {self.user}'
