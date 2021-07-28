
from django import forms
from .models import Order
class OrderCreateForm(forms.ModelForm):
     
    #  user_id=forms.CharField(widget=forms.HiddenInput())        
    #  Quantity=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}),label_suffix='',label='Quantity')
     class Meta:
      model = Order
      fields = [ 'Order_Name_Of_Product', 'Order_Quantity','Phone','Email']


class OrderUpdateForm(forms.ModelForm):
     
     class Meta:
      model = Order
      fields = [ 'Order_Name_Of_Product', 'Order_Quantity','Phone','Email']