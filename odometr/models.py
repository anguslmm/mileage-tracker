from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=50)
    initial_mileage = models.PositiveIntegerField()
    start_date = models.DateTimeField('date started')
    yearly_mileage = models.PositiveIntegerField()
    end_date = models.DateTimeField('date ends')
    def __str__(self):
        return self.name

class Checkpoint(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    mileage = models.PositiveIntegerField()
    log_date = models.DateTimeField('date of mileage')
    def __str__(self):
        return "{} miles on {}".format(self.mileage, self.log_date.strftime("%a %b %d %H:%M:%S %Y"))