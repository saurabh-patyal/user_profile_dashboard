from django.contrib import admin
from .models import Product,Category,Order
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id' , 'Category_Name','Created_Date')
    list_display_links=('id','Category_Name')
    
    list_filter=('Created_Date','Category_Name')
    list_per_page=20
    search_fields=('Created_Date','Category_Name')




admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=('id' , 'Product_Name','Product_Quantity','Product_Category','Created_by','Created_Date')
    list_display_links=('id','Product_Name')
    list_editable=('Product_Quantity',)
    list_filter=('Created_Date','Product_Name')
    list_per_page=20
    search_fields=('Created_Date','Product_Name','Created_by')




admin.site.register(Product,ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display=('id' , 'Order_Name_Of_Product','Order_Quantity','Created_Date')
    list_display_links=('id','Order_Name_Of_Product')
    list_editable=('Order_Quantity',)
    list_filter=('Order_Name_Of_Product',)
    list_per_page=20
    search_fields=('Created_Date','Order_Name_Of_Product')




admin.site.register(Order,OrderAdmin)