from django.contrib import admin
from .models import Category,Stock
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id' , 'Category_Name','Created_Date')
    list_display_links=('id','Category_Name')
    
    list_filter=('Created_Date','Category_Name')
    list_per_page=20
    search_fields=('Created_Date','Category_Name')




admin.site.register(Category,CategoryAdmin)

class StockAdmin(admin.ModelAdmin):
    list_display=('id' , 'Item_Name','Quantity','Receive_by','Phone_Number','Created_Date')
    list_display_links=('id','Item_Name')
    list_editable=('Quantity',)
    list_filter=('Created_Date','Item_Name')
    list_per_page=20
    search_fields=('Created_Date','Item_Name')




admin.site.register(Stock,StockAdmin)
