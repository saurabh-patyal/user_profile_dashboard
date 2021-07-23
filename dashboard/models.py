from django.db import models
from datetime import datetime
# Create your models here.
# Create your models here.

class Category(models.Model):
    Category_Name=models.CharField(max_length=50,blank=True)
    Created_Date=models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.Category_Name



class Stock(models.Model):
	Category = models.ForeignKey(Category,null=True,on_delete=models.CASCADE)
	Item_Name = models.CharField(max_length=50,blank=True)
	Quantity = models.IntegerField(default='0',blank=True)
	Receive_quantity = models.IntegerField(default='0', blank=True, null=True)
	Receive_by = models.CharField(max_length=50, blank=True, null=True)
	Issue_quantity = models.IntegerField(default='0', blank=True, null=True)
	Issue_by = models.CharField(max_length=50, blank=True, null=True)
	Issue_to = models.CharField(max_length=50, blank=True, null=True)
	Phone_Number = models.CharField(max_length=50, blank=True, null=True)
	Created_by = models.CharField(max_length=50, blank=True, null=True)
	Reorder_level = models.IntegerField(default='0', blank=True, null=True)
	Created_Date = models.DateTimeField(auto_now_add=False, auto_now=True)
	Export_to_CSV = models.BooleanField(default=False)

	def __str__(self):
		return self.Item_Name
