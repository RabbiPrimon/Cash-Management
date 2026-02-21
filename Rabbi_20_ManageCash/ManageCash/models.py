from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
  def __str__(self):
    return self.username


class AddCashModel(models.Model):
  user = models.ForeignKey(CustomUserModel,on_delete=models.CASCADE,related_name='profile_info',null=True)
  source = models.CharField(max_length=250,null=True)
  datetime = models.DateField( auto_now_add=True,null=True)
  amount = models.DecimalField(max_digits=10, decimal_places=2, default=0,null=True)
  description = models.TextField(null=True)
  def __str__(self):
    return self.user
  
class ExpenseModel(models.Model):
  user = models.ForeignKey(CustomUserModel,on_delete=models.CASCADE,related_name='expense_user',null=True)
  description = models.TextField(null=True)
  amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
  datetime = models.DateField(auto_now_add=True, null=True)
  
  def __str__(self):
    return str(self.amount)


