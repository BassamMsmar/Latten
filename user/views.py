from django.forms.models import construct_instance
from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def signin(request):
    if request.method == 'POST':
        form = forms.FormRegisterUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')

    else:
        form = forms.FormRegisterUser()
    
    context = {'form':form}
    return render(request, 'user/form-register-user.html', context)


