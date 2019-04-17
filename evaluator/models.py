from django.db import models

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=50)
    def __str__(self):
        return self.company_name
    
      

class Company_Field(models.Model):
    company = models.ForeignKey(Company, on_delete = models.CASCADE)
    field_name = models.CharField(max_length=50)
    field_minimum_score = models.IntegerField(default=50)
    def __str__(self):
        return self.field_name

class User(models.Model):
    user_name = models.CharField(max_length=50)
    def __str__(self):
        return self.user_name
    
      

class User_Field(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    field_name = models.CharField(max_length=50)
    field_test_score = models.IntegerField(default=0)
    def __str__(self):
        return self.field_name


