from django.db import models

# Create your models here.
class Add(models.Model):
    num1 = models.FloatField()
    num2 = models.FloatField()

    def __str__(self):
        return 'Result for  ' + str(self.num1) + "& " + str(self.num2)

class Subtract(models.Model):
    num1 = models.FloatField()
    num2 = models.FloatField()

    def __str__(self):
        return 'Result for  ' + str(self.num1) + "& " + str(self.num2)

class Multiply(models.Model):
    num1 = models.FloatField()
    num2 = models.FloatField()

    def __str__(self):
        return 'Result for  ' + str(self.num1) + "& " + str(self.num2)

class Divide(models.Model):
    num1 = models.FloatField()
    num2 = models.FloatField()

    def __str__(self):
        return 'Result for  ' + str(self.num1) + "& " + str(self.num2)
