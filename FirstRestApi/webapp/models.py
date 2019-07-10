from django.db import models

class Employee(models.Model):
    employee_id = models.IntegerField()
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name
