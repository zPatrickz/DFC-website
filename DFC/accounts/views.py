from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from forms import OrganizationCreationForm, UserCreationForm


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

@login_required
def user_profile(request):
    pass
    #if request.method == 'POST':
    #    form = UserProfileForm(request.POST, instance=request.user.profile)
    #    if form.is_valid():
    #        form.save()
    #        return HttpResponseRedirect('accounts/profile.html')
    #else:
    #    form = UserProfileForm(instance=request.user.profile)
    #return render_to_response('accounts/profile.html', {
    #    'form': form,
    #    'user': request.user,
    #    }, context_instance=RequestContext(request))
