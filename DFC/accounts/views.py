from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from forms import UserProfileForm
from models import UserProfile


def register(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        form = UserCreationForm(request.POST)
        errors = []
        if not form.is_valid():
            errors.extend(UserCreationForm.error_messages)
            print UserCreationForm.error_messages
            return HttpResponseRedirect('/accounts/register', {'errors': errors, })
        user = form.save()
        user.save()
        user_profile = UserProfile(user=user)
        user_profile.save()
        new_user = auth.authenticate(username=username, password=password)
        if new_user is not None:
            auth.login(request, new_user)
            return HttpResponseRedirect('/accounts/profile')
        else:
            return HttpResponseRedirect('/accounts/login')

    form = UserCreationForm()
    return render_to_response("registration/register.html", {
        'form': form,
    }, context_instance=RequestContext(request))


def show_profile(request):
    user = request.user
    if user.is_authenticated() and user.is_active:
        profile = UserProfile.objects.get(user=user)
        form = UserProfileForm(instance=profile)
        return render_to_response('profile.html', {
            'form': form,
        }, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/accounts/login')