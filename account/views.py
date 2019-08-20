from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse
from .models import User
from .forms import RegisterForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(username=username, password=password)
        return HttpResponseRedirect(reverse('account:login'))
    else:
        form = RegisterForm()
        return render(request, 'account/register.html', {'form': form})