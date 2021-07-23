
from django import forms
from .models import Stock
class StockCreateForm(forms.ModelForm):
     
    #  Item_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item Name'}),label_suffix='',label='Item Name')        
    #  Quantity=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}),label_suffix='',label='Quantity')
     class Meta:
      model = Stock
      fields = ['Category', 'Item_Name', 'Quantity']


class StockUpdateForm(forms.ModelForm):
     
     class Meta:
      model = Stock
      fields = ['Category', 'Item_Name', 'Quantity']