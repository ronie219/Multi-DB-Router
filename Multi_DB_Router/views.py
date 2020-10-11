from django.views.generic import CreateView
from django.shortcuts import redirect,render
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from accounts.models import CustumUser
from accounts.models import Product_1
from product2.models import Product_2
from product3.models import Product_3
from product4.models import Product_4
from product5.models import Product_5
from .forms import CustomUserForm, AccountCreationForm

@login_required
def UserCreation(request):

    if request.method == 'POST':
        user_creation = AccountCreationForm(request.POST)
        database_form = CustomUserForm(request.POST)
        if user_creation.is_valid() and database_form.is_valid():
            obj = user_creation.save()
            db = database_form.save(commit=False)
            db.user = obj
            db.save()
            messages.success(request, 'Account created successfully')
            send_mail('Success', 'Account created successfully. and Your usersname is {}'.format(obj.username), 'abhishek.biswas219@gmail.com', [obj.email])
            return redirect('account-creation')
    else:
        user_creation = AccountCreationForm()
        database_form = CustomUserForm()
    context = {'form1': user_creation, 'form2': database_form}
    return render(request, 'userCreation.html', context )


def Home(request):
    try:
        qs = CustumUser.objects.filter(user = request.user)
    except TypeError:
        qs = {}
    return render(request, 'index.html',{'data' : qs})


@login_required
def ProductCreation(request):
    try:
        qs = CustumUser.objects.filter(user = request.user)
    except TypeError:
        qs = {}
    if request.method == 'POST':
        db_name = (request.POST.get('database'))
        product_name = (request.POST.get('productName'))
        if db_name=='database1':
            Product_1.objects.create(name=product_name,database_name = db_name,username=request.user) 
        elif db_name=='database2':
            Product_2.objects.using(db_name).create(name=product_name,database_name = db_name,username=request.user) 
        elif db_name=='database3':
            Product_3.objects.using(db_name).create(name=product_name,database_name = db_name,username=request.user) 
        elif db_name=='database4':
            Product_4.objects.using(db_name).create(name=product_name,database_name = db_name,username=request.user) 
        elif db_name=='database5':
            Product_5.objects.using(db_name).create(name=product_name,database_name = db_name,username=request.user) 
        else:
            return render(request, 'product_creation.html', {'data' : qs,'message':'No database Insert'} )

        return render(request, 'product_creation.html', {'data' : qs,'message':'product Created Succesfully'} )
    else:
        return render(request, 'product_creation.html', {'data' : qs} )

@login_required
def ProductList(request):
    context = {}
    qs1 = Product_1.objects.filter(username=request.user).using('default').order_by('-username')
    context['qs1'] = qs1
    qs2 = Product_2.objects.filter(username=request.user).using('database2')
    context['qs2'] = qs2
    qs3 = Product_3.objects.filter(username=request.user).using('database3')
    context['qs3'] = qs3
    qs4 = Product_4.objects.filter(username=request.user).using('database4')
    context['qs4'] = qs4
    qs5 = Product_5.objects.filter(username=request.user).using('database5')
    context['qs5'] = qs5
    return render(request,'product_list.html',context)

@login_required
def UserList(request):
    context = {}
    context['product1'] = Product_1.objects.all()
    context['product2'] = Product_2.objects.all().using('database2')
    context['product3'] = Product_3.objects.all().using('database3')
    context['product4'] = Product_4.objects.all().using('database4')
    context['product5'] = Product_5.objects.all().using('database5')
    return render(request,'user_list.html',context)

@login_required
def deleteProduct(request,pk,db):
    if request.method == 'POST':
        if db=='database1':
            Product_1.objects.get(id=pk).delete() 
        elif db=='database2':
            Product_2.objects.using(db).get(id=pk).delete(using=db)
        elif db=='database3':
            Product_3.objects.using(db).get(id=pk).delete(using=db)
        elif db=='database4':
            Product_4.objects.using(db).get(id=pk).delete(using=db)
        elif db=='database5':
            Product_5.objects.using(db).get(id=pk).delete(using=db)
        return redirect('user-list')
    else:
        return render(request, 'confirm-delete.html',{'pk':pk,'db':db})


@login_required
def editProduct(request,pk,db,name):
    if request.method == 'POST':
        product_name = (request.POST.get('productName'))
        if db=='database1':
            p = Product_1.objects.get(id=pk)
            p.name = product_name
            p.save()
        elif db=='database2':
            p = Product_2.objects.using(db).get(id=pk)
            p.name = product_name
            p.save(using=db)
        elif db=='database3':
            p = Product_3.objects.using(db).get(id=pk)
            p.name = product_name
            p.save(using=db)
        elif db=='database4':
            p = Product_4.objects.using(db).get(id=pk)
            p.name = product_name
            p.save(using=db)
        elif db=='database5':
            p = Product_5.objects.using(db).get(id=pk)
            p.name = product_name
            p.save(using=db)
        return redirect('user-list')
    else:
        return render(request, 'product_edit.html',{'product_name':name})