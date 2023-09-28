from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Hadith
from .forms import HadithForm
from .filters import HadithFilter
from .forms import CreateUserForm, ProfileForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import  unauthenticated_user


# Create your views here.
#login function
def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) #after this request.user = user as long as logged in. 
            return redirect ('/hadith/')
        else:
            attempt = request.session.get('attempt') or 0
            request.session['attempt'] = attempt + 1
            request.session['invalid_user'] = 1 # 1 == True
    return render(request, 'app/form.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('/hadith/')


def profile_setting(request):
    user = request.user
    form = ProfileForm(instance=user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
    context = {'form': form}
    return render(request, 'app/setting.html', context)


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,f'Account is created for {user}.')
            return redirect('/')
    context ={
        'form': form,
    }
    return render(request, 'app/register.html', context)

@unauthenticated_user
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            messages.success(request,f'{user.username} successfully logged in!')
            return redirect('/')
        else:
            message = messages.info(request,'username and/or password are incorrect.')
    context={}
    return render(request, 'app/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/')


def home(request):
    return render(request, 'app/home.html')


def hadith_detail(request, pk):
    hadith = Hadith.objects.get(id=pk)
    context={
        'hadith': hadith
    }
    return render(request, 'app/detail.html', context)

def search(request):
    query = request.GET.get('q')
    query_set = Hadith.objects.all()
    if query is not None:
        lookups = Q(id__icontains=query)|Q(title__icontains=query)|Q(detail__icontains=query)|Q(tag__icontains=query)
        query_set = Hadith.objects.filter(lookups)
    context={
        'query_set': query_set
    }
    return render(request, 'app/search.html', context)

#searching method using django-filter extenstion
def hadith(request):
    hadiths = Hadith.objects.all()
    myfilter = HadithFilter(request.GET,queryset=hadiths)
    hadiths = myfilter.qs
    context = {
        'hadiths': hadiths, 
        'myfilter': myfilter,
    }
    return render(request, 'app/hadith.html', context)

def create(request): 
    form = HadithForm()
    if request.method == 'POST':
        form = HadithForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/hadith/')
    context = {
        'form':form
    }
    return render(request, 'app/create.html', context)

def update(request, pk): 
    hadith = Hadith.objects.get(id=pk)
    form = HadithForm(instance=hadith)
    if request.method == 'POST':
        form = HadithForm(request.POST, instance=hadith)
        if form.is_valid():
            form.save()
            return redirect('/hadith/')
    context = {
        'form': form,
        }
    return render(request, 'app/create.html', context)

def delete(request, pk):
    hadith = Hadith.objects.get(id=pk)
    if request.method == 'POST':
        hadith.delete()
        return redirect('/hadith/')
    context = {'hadith': hadith}
    return render(request, 'app/delete.html', context)