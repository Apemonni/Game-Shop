from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, DevRegisterForm
from .models import Profile, DevProfile


def pre_register(request):
    return render(request, 'users/register_start.html')


def register(request, user_type):
    is_dev = user_type=='developer'
    if request.method == 'POST':
        form = DevRegisterForm(request.POST) if is_dev else UserRegisterForm(request.POST)

        if form.is_valid():

            user = form.save()
            if is_dev:
                profile = DevProfile.objects.create(user=user, is_dev=is_dev, seller_id=form.data['seller_id'], secret_key=form.data['secret_key'] )
            else:
                profile = Profile.objects.create(user=user, is_dev=is_dev)
            profile.save()

            return redirect('login')
    else:
        form = DevRegisterForm if is_dev else UserRegisterForm()

    return render(request, 'users/register.html', { 'form': form })


