from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth.models import User
import requests
from news_blog_app.settings import API_KEY
# Create your views here.

# def mockLogin(request):
#     return render(request, 'login_register.html')

def loginUser(request):
    page='login'

    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist")
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect(request.GET['next'] if 'next' in request.GET else 'news')
        else:
            messages.error(request, "Username or Password is incorrect.")
    return render(request, "login_register.html")


def logoutUser(request):
    logout(request)
    messages.info(request, "User was logged out!")
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "User account was created.")
            login(request, user)
            return redirect('edit-account')
        
        else:
            messages.error(request, "An error has occured during the registration.")
        
    context = {'page':page, 'form': form}
    return render(request, 'login_register.html', context)

@login_required(login_url="login")
def userAccount(request):
    profile = request.user.profile
    blogs = profile.blog_posts.all()
    context = {'profile': profile, 'blogs': blogs}
    return render(request, 'account.html', context)

@login_required(login_url='login')
def editAccount(request):
    profile =  request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')
    
    context = {'form':form}
    return render(request, 'profile_form.html', context)



@login_required(login_url='login')
def news(request):
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    news = response.json()
    # print(response.text)
    articles = news['articles']
    title = []
    description = []
    url = []

    imgUrl = []
    for i in range(len(articles)):
        current = articles[i]
        title.append(current['title'])
        description.append(current['description'])
        url.append(current['url'])
        imgUrl.append(current['urlToImage'])
    top_headlines = zip(title, description, url, imgUrl)

    context = {'top_headlines': top_headlines}
    return render(request,'news.html', context)

def dashboard(request):
    return render(request, 'dashboard.html')