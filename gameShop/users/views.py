from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import PlayerRegisterForm, DevRegisterForm


def register(request):

    if request.method == 'POST':
        form = PlayerRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = PlayerRegisterForm()

    return render(request, 'users/register.html', { 'form':form })

