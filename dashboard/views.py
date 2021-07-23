from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Stock
from .forms import StockCreateForm,StockUpdateForm
from django.contrib import messages
from django.utils.safestring import mark_safe
# Create your views here.
#############user dashboard######################
@login_required(login_url='login')   
def dashboard(request):
    Query_set=Stock.objects.all()
        
    #Logic for search by category & productname
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
            #join query from 2 columns of one table for search by category & productname
            Query_set=Query_set.filter(Item_Name__icontains=keywords)

    
    context={
        'products':Query_set
    }

    return render(request,'accounts/dashboard.html',context)

    
#############user Create Order######################
@login_required(login_url='login')   
def order(request):
    if request.method == 'POST':
        form=StockCreateForm(request.POST)
        if form.is_valid():
            Item_name=form.cleaned_data['Item_Name']
            Category=form.cleaned_data['Category']
            Quantity=form.cleaned_data['Quantity']
            form.save()        
            messages.success(request,'Item is Ordered Successfully')
            return redirect('dashboard')
        else:
            form=StockCreateForm(request.POST)
            context={
            'form':form,
            
        }
            
            return render(request,'accounts/add_order.html',context)
    
    form=StockCreateForm()
    context={
        'form':form
    }

    return render(request,'accounts/add_order.html',context)

#########User Edit order############
def editorder(request,pk):
    queryset = Stock.objects.get(id=pk)
    form = StockUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = StockUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request,mark_safe("your order Is Successfully Updated <a href='{% url 'editorder instance.id' %}'>View</a>"))
            return redirect('dashboard')
         
    context = {
        'form':form,
        'pk':pk
        
    }
    return render(request,'accounts/edit_order.html', context)

#################Delete Order###############
def deleteorder(request,pk):
    queryset = Stock.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request,'Item is Deleted Successfully')
        return redirect('dashboard')
    context={
        'pk':pk
    }
    return render(request, 'accounts/del_order.html',context)