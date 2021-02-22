from django.shortcuts import render, redirect
from .models import Posts
from .forms import  FormPost

# Create your views here.
def posts(request):
    posts = Posts.objects.all()
    context = {'posts':posts}
    return render(request, 'posts/list-posts.html', context) 


def add_post(request):
    if request.method == 'POST':
        form = FormPost(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
            
    else:
        form = FormPost()   

    context = {'form':form}
    return render(request, 'posts/add-post.html', context)