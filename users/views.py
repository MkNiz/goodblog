from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def logout_view(request):
    """Log a user out"""
    logout(request)
    return HttpResponseRedirect(reverse('blog:index'))

def register(request):
    """Registers a new user"""
    if request.method != 'POST':
        # Displays blank registration form
        form = UserCreationForm()
    else:
        # Process the completed form
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Log user in and redirect to home
            auth_user = authenticate(username=new_user.username,
                password=request.POST['password1'])
            login(request, auth_user)
            return HttpResponseRedirect(reverse('blog:index'))
    return render(request, 'users/register.html', { 'form': form })
