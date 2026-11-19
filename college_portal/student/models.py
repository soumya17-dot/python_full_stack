from django.db import models

# Create your models here.
class Student_table(models.Model):
    reg_no=models.IntegerField(primary_key=True)
    name=models.CharField()
    email=models.EmailField()
    marks=models.DecimalField(max_digits=6,decimal_places=2)
    dob=models.DateField()

    def __str__(self):
        return self.name