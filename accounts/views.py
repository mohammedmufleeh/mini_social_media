from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm,ImageForm
from . models import Image,Comment

def signup_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_login')
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm(request)
    return render(request, 'login.html', {'form': form})

def home(request):
    images = Image.objects.prefetch_related('users').all()
    return render(request, 'home.html',{'images': images})

def logout_view(request):
    logout(request)
    return redirect('home')



def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.save()
            image.users.add(request.user)
            return redirect('home')
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})

@login_required
def add_comment(request, pk):
    photo = get_object_or_404(Image, pk=pk)

    if request.method == 'POST':
        text = request.POST.get('text')
        comment = Comment.objects.create(photo=photo, author=request.user, text=text)
        return redirect('add_comment', pk=photo.pk)

    return render(request, 'photo_detail.html', {'photo': photo})

