from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from forms import UserProfileForm, OrganizationForm
from models import UserProfile
from django.contrib.auth.decorators import login_required


def register(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        form = UserCreationForm(request.POST)
        errors = []
        if not form.is_valid():
            errors.extend(UserCreationForm.error_messages)
            return HttpResponseRedirect('/accounts/register', {'errors': errors, })
        user = form.save()
        user.save()
        profile = UserProfile(user=user)
        profile.save()
        new_user = auth.authenticate(username=username, password=password)
        if new_user is not None:
            auth.login(request, new_user)
            return HttpResponseRedirect('/accounts/profile')
        else:
            return HttpResponseRedirect('/accounts/login')

    form = UserCreationForm()
    return render_to_response("accounts/register.html", {
        'form': form,
    }, context_instance=RequestContext(request))


def signup_organization(request):
    singup_form = OrganizationForm()
    return render_to_response('accounts/organization_signup.html', {
        'form': singup_form,
    })


@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('accounts/profile.html')
    else:
        form = UserProfileForm(instance=request.user.profile)
    return render_to_response('accounts/profile.html', {
        'form': form,
        'user': request.user,
        }, context_instance=RequestContext(request))
