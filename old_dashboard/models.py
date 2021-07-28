from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
# Create your models here.


# Create your models here.
class Category(models.Model):
    Category_Name = models.CharField(max_length=50, blank=True)
    Created_Date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.Category_Name


class Product(models.Model):
    Product_Name = models.CharField(max_length=100, null=True)
    Product_Quantity = models.PositiveIntegerField(null=True)
    Product_Cat = models.ForeignKey(Category,null=True,on_delete=models.CASCADE)
    Created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Created_Date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'{self.Product_Name}'


class Order(models.Model):
    Order_Name_Of_Product = models.ForeignKey(Product,
                                              on_delete=models.CASCADE,
                                              null=True)
    OrderBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # IssueBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # IssueTo = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Order_Quantity = models.PositiveIntegerField(null=True)
    Issued_Quantity = models.IntegerField(default='0', blank=True, null=True)

    def __str__(self):
        return f'{self.Order_Name_Of_Product}-{self.Order_By}'