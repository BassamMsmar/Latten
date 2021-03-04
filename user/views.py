from django.contrib.auth.views import PasswordResetConfirmView
from django.forms.models import construct_instance
from django.shortcuts import render, redirect

from .forms import FormRegisterUser
from posts.models import Posts


# Create your views here.
def signin(request):
    if request.method == 'POST':
        form = FormRegisterUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = FormRegisterUser()
    
    context = {'form':form}
    return render(request, 'registration/form-register-user.html', context)

def profile(request):
    posts = Posts.objects.filter(content=request.user)
    context = {'posts':posts}
    return render(request, 'registration/profile.html', context)
