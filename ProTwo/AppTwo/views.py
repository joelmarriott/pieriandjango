from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from AppTwo.models import User
# Create your views here.

def index(request):
    form = forms.AddUser()

    if request.method == 'POST':
        form = forms.AddUser(request.POST)

    if form.is_valid():
         print('VALIDATION SUCCESS')
         print('FIRST NAME: '+form.cleaned_data['firstName'])
         print('LAST NAME: '+form.cleaned_data['lastName'])
         print('EMAIL: '+form.cleaned_data['email'])
         form.save()


    return render(request,'index.html',{'form':form})



def help(request):
    my_dict = {'help':'Help Page'}
    return render(request,'help.html',context=my_dict)


def user(request):
    user_list = User.objects.order_by('firstName')
    user_dict = { 'users':user_list }
    return render(request,'user.html',context=user_dict)
