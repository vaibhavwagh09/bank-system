from os import name
from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse
from home.models import Users , Transfer
from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request,'index.html')

def about_us(request):
    return render(request,'about_us.html')

def Add_users(request):
    if request.method == "POST" :
        account_num = request.POST['account_number']
        name_c = request.POST['name']
        phone_num = request.POST['phone_number']
        balance_c  = request.POST['balance']
        inst = Users(account_number=account_num,name=name_c, phone_number=phone_num, balance=balance_c )                                            
        inst.save()
        return redirect('users')
    return render(request,'Add_users.html')


def transactions(request):
    alltransactions = Transfer.objects.all()
    context = {'transactions': alltransactions}
    return render(request,'transactions.html',context)

def users(request):
    allUsers = Users.objects.all()
    context = {'users': allUsers}
    return render(request, 'users.html',context)

def payment(request,pk):
    sender = Users.objects.get(id=pk)
    
    if request.method == 'POST':
        try:
            usr = request.POST.get('fromuser')
            tou = request.POST.get('to_user')
            amount_user = request.POST.get('amount')
            amt = int(amount_user)

           
            with transaction.atomic():
                from_user_obj = Users.objects.get(name=usr)
                from_user_obj.balance -= int(amount_user)
                from_user_obj.save()

                to_user_obj = Users.objects.get(name=tou)
                to_user_obj.balance += int(amount_user)
                to_user_obj.save()

                ins = Transfer(from_cust=usr,to_cust=tou,cust_amount=amt)
                ins.save()
                messages.success(request, 'Your amount is transferred')
                return redirect('transactions')

        except Exception as e:
            print(e) 
            messages.error(request, 'Something is wrong')

    return render(request, 'payment.html', {'sender': sender})
