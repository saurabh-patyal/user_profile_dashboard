from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product,Order,Category
from .forms import OrderCreateForm,OrderUpdateForm
from django.contrib import messages


############################## View for retreaive & display all entries from Product table & Serach##########.
@login_required(login_url='login')
def dashboard(request):
    Query_set = Product.objects.all()
   

    # Logic for search by category & product by name
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            # join query from 2 columns of one table for search by category & productname
            Query_set = Query_set.filter(Product_Name__icontains=keywords) | Query_set.filter(
                Product_Category__Category_Name__icontains=keywords)  # For accessing other table when have relationship field EX->Modal__columnname like Category__Category_Name

    context = {
        'products': Query_set
    }

    return render(request, 'accounts/dashboard.html', context)
    
##################################### Single Product Page########################################
@login_required(login_url='login')
def productDetail(request,pk):
    Product_Detail = get_object_or_404(Product,id=pk)
    context={ 
        'product': Product_Detail
    }

    return render(request,'accounts/product_detail.html',context)
    
#################################################Orders Management########################################################
   
############################################Create Orders##############################
    
@login_required(login_url='login')
def addOrder(request):
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        
        if form.is_valid():
            Order_Name_Of_Product = form.cleaned_data['Order_Name_Of_Product']
            Order_Quantity = form.cleaned_data['Order_Quantity']
            Phone = form.cleaned_data['Phone']
            Email = form.cleaned_data['Email']
            # print(Order_Name_Of_Product)
            instance = form.save(commit=False) #By this you can take form value to variable like order.then you will process data from database like.order.customer=request.user
            # print(instance.Order_Name_Of_Product.Product_Quantity)
            # print(instance.Order_Quantity)
            

            instance.customer = request.user  #Logic to have the logged-in user and saving in user field of instance table
            instance.save()
            messages.success(request, 'Item is Ordered Successfully')
            return redirect('viewOrders')
        else:
            form = OrderCreateForm(request.POST)
            context = {
                'form': form,

            }

            return render(request, 'accounts/add_order.html', context)

    form = OrderCreateForm()
    context = {
        'form': form
    }

    return render(request, 'accounts/add_order.html', context)


############################## View for  display all Orders from Order table For loggedin users & Search##########.
@login_required(login_url='login')
def viewOrders(request):
    Query_set = Order.objects.filter(customer_id=request.user.id) #Query to fetch specific user's orders
    context = {
        'orders': Query_set
    }

    return render(request, 'accounts/view_orders.html', context)


################################ View for  Update Orders from Order table For loggedin users######################.
@login_required(login_url='login')
def editOrder(request,pk):
    # user=Order.objects.filter(customer_id=request.user.id)
    query_set = Order.objects.get(id=pk)  ####objects.get method doesnot return queryset like filter.It will return onlny one result
    form = OrderUpdateForm(instance=query_set)
    if request.method == 'POST':
        form = OrderUpdateForm(request.POST, instance=query_set)
        if form.is_valid():
            form.save()
            messages.success(request,'Item is Updated Successfully')       
            return redirect('viewOrders')
         
    context = {
        'form':form,
        'pk':pk
        
    }
    return render(request,'accounts/edit_order.html', context)


################################ View for  Delete Orders from Order table For loggedin users###################.

def deleteOrder(request,pk):
    queryset = Order.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('viewOrders')
    context={
        'pk':pk
    }
    return render(request, 'accounts/del_order.html',context)
