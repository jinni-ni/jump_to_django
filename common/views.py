from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from common.forms import UserForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data_get('username')
            raw_password = form.cleaned_data_get('password1')
            user = authenticate(username=username, raw_password=raw_password)
            login(redirect, user)
            return redirect('index')
        
    else:
        form = UserForm()
        
    return render(request, 'common/signup.html', {'form' : form})
