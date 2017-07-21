# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from datetime import datetime
from demoapp.forms import SignUpForms,LoginForm
from demoapp.models import UserModel
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForms(request.POST)
        if form.is_valid():
            Username = form.cleaned_data['Username']
            Email =form.cleaned_data['Email']
            Name = form.cleaned_data['Name']
            Password = form.cleaned_data['Password']
            # insert data to db
            new_user = UserModel(Name=Name,Password=make_password(Password),Username=Username, Email=Email)
            new_user.save()
            return render(request,'success.html')
    else:
        form = SignUpForms()
    return render(request,'register.html',{'form':form})


def login_view(request):
    if request.method == 'GET':
        #Display Login Page
        login_form = LoginForm()
        template_name = 'login.html'
    elif request.method == 'POST':
        #Process The Data
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            #Validation Success
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            #read Data From db
            user = UserModel.objects.filter(username=username).first()
            if user:
                #compare Password
                if check_password(password, user.password):
                    #successfully Login
                    template_name = 'login_success.html'
                else:
                    #Failed
                    template_name = 'login_fail.html'
            else:
                #user doesn't exist
                template_name = 'login_fail.html'
        else:
            #Validation Failed
            template_name = 'login_fail.html'


    return render(request,template_name,{'login_form':login_form})