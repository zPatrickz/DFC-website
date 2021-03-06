from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from forms import *

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            if request.user.is_authenticated():
                auth_logout(request)
            user = authenticate(email=request.POST['email'], password=request.POST['password'])
            auth_login(request, user)
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'accounts/register.html', {
        'form': form,
    })

def register_organization(request):
    form = OrganizationCreationForm()
    if request.method == 'POST':
        form = OrganizationCreationForm(request.POST)
        if form.is_valid():
            form.save()
            if request.user.is_authenticated():
                auth_logout(request)
            organization = authenticate(email=request.POST['email'], password=request.POST['password'])
            auth_login(request, organization)
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'accounts/organization_register.html', {
            'form': form,
    })

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))
    form = SignInForm()
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email, password, remember_me = (form.cleaned_data['email'], 
                form.cleaned_data['password'], 
                form.cleaned_data['remember_me'])
            user = authenticate(email=email, password=password)
            auth_login(request, user)
            if remember_me:
                request.session.set_expiry(24*60*60)
            else:
                request.session.set_expiry(0)
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'accounts/login.html', {
        'form': form, 
    })

def logout(request):
    if request.user.is_authenticated():
        auth_logout(request)
        return HttpResponseRedirect(reverse('index'))

@login_required
def user_profile(request):
    if request.user.is_organization:
        return render(request, 'accounts/organization_profile.html')
    return render(request, 'accounts/profile.html')
    
@login_required
def user_message(request):
    return render(request, 'accounts/messages.html')
    
@login_required
def user_settings(request):
    form = OrganizationSettingsForm()
    if request.user.is_organization:
        return render(request, 'accounts/organization_settings.html', {
            'form': form, 
        })
    return render(request, 'accounts/settings.html', {
        'form': form, 
    })

