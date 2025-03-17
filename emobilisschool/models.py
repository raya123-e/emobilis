from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=50)
    adm=models.IntegerField()
    date=models.DateField()
    form=models.CharField(max_length=50)



    def __str__(self):
        return self.name
class Teachers(models.Model):
    name=models.CharField(max_length=15)
    age=models.IntegerField()
    email=models.EmailField()
    department=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)

    def __str__(self):
        return self.name+" "+self.status

class Parents(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    phonenumber=models.IntegerField()
    email=models.EmailField()
  

    def __str__(self):
        return self.firstname+" "+self.lastname


# mpesa API
class Transaction(models.Model):
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=[('Success', 'Success'), ('Failed', 'Failed')])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone_number} - {self.amount} - {self.status}"