from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm#PlayerRegisterForm, DevRegisterForm
from .models import Profile


def pre_register(request):
    return render(request, 'users/register_start.html')


def register(request, user_type):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            user = form.save()
            profile = Profile.objects.create(user=user, is_dev=user_type=='developer')
            profile.save()

            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', { 'form': form })


