from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required 
from .utils import paginateProjects, searchBlogs
from .forms import BlogForm
from django.contrib import messages

# Create your views here.

def blogs(request):
    blogs, search_query = searchBlogs(request)
    custom_range,blogs = paginateProjects(request, blogs, 6)

    context = {'blogs': blogs, 'search_query': search_query, 'custom_range': custom_range}

    return render(request, 'blogs.html', context)


def blog(request, pk):
    blogObj = Post.objects.get(id=pk)
    
    # Todo:  add commenting feature later if required 
    context = {'blog': blogObj}
    return render(request, 'single-blog.html', context)
        
@login_required(login_url="login")
def createBlog(request):
    profile = request.user.profile
    form = BlogForm
    if request.method=="POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = profile
            blog.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'blog_form.html', context)
    
@login_required(login_url='login')
def updateBlog(request, pk):
    profile = request.user.profile
    blog = profile.blog_posts.get(id=pk)
    form = BlogForm(instance=blog)

    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)

        if form.is_valid():
            form.save()
            return redirect("account")
    
    context = {'form': form, 'blog': blog}
    return render(request, 'blog_form.html', context)


@login_required(login_url='login')
def deleteBlog(request, pk):
    profile = request.user.profile
    blog = profile.blog_posts.get(id=pk)
    if request.method=="POST":
        blog.delete()
        return redirect('blogs')
    context = {'object': blog}
    return render(request, 'delete_template.html', context)
