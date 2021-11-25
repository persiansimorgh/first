from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .form import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render,redirect
from .models import Videos
from .models import Post

# Create your views here.

def upload_video(request):
    
    if request.method == 'POST': 
        
        name = request.POST['name']
        video = request.POST['video']
        
        content = Videos(name=name,video=video)
        content.save()
        return redirect('dashboard')
    
    return render(request,'upload.html')


def display(request):
    
    videos = Videos.objects.all()
    context ={
        'videos':videos,
    }
    
    return render(request,'videos.html',context)






@user_passes_test(lambda user: user.is_staff)
def staff_place(request):
    return HttpResponse("Employees must wash hands", content_type="text/plain")






@login_required
def private_place(request):
    return HttpResponse("It's banned for you", content_type="text/plain")



def dashboard(request):
    return render(request, "blog/dashboard.html")


def register(request):
    if request.method == "POST":
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully')
            login(request, user)
            return redirect("dashboard")
            
    else:
        f = CustomUserCreationForm()
    return render(request, 'blog/register.html',{'form': f})   
            
            
            
            

                   
def listing(request):
    data = {
        "blogs": Post.objects.all(),
    }

    return render(request, "listing.html", data)

def view_blog(request, blog_id):
    blog = get_object_or_404(Post, id=blog_id)
    data = {
        "blog": blog,
    }

    return render(request, "view_blog.html", data)




def user_info(request):
    text = f"""
        Selected HttpRequest.user attributes:

        username:     {request.user.username}
        is_anonymous: {request.user.is_anonymous}
        is_staff:     {request.user.is_staff}
        is_superuser: {request.user.is_superuser}
        is_active:    {request.user.is_active}
    """

    return HttpResponse(text, content_type="text/plain")           


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})



def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

