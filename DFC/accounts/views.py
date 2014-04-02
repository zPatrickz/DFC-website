from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from forms import OrganizationCreationForm, UserCreationForm, SignInForm


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    return render_to_response('accounts/register.html', {
        'form': form,
    }, context_instance=RequestContext(request))

def signup_organization(request):
    form = OrganizationCreationForm()
    if request.method == 'POST':
        form = OrganizationCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    return render_to_response('accounts/organization_signup.html', {
            'form': form,
    }, context_instance=RequestContext(request))

def login(request):
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
    return render_to_response('accounts/login.html', {
        'form': form, 
    }, context_instance=RequestContext(request))

def logout(request):
    if request.user.is_authenticated():
        auth_logout(request)
        return HttpResponseRedirect(reverse('index'))

@login_required
def user_profile(request):
    pass
