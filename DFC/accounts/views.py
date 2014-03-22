from django.shortcuts import render_to_response
from forms import OrganizationSignUpForm
from django.contrib.auth.decorators import login_required
from django.template import RequestContext


def register(request):
    pass
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password1')
    #     form = UserCreationForm(request.POST)
    #     errors = []
    #     if not form.is_valid():
    #         errors.extend(UserCreationForm.error_messages)
    #         return HttpResponseRedirect('/accounts/register', {'errors': errors, })
    #     user = form.save()
    #     user.save()
    #     profile = UserProfile(user=user)
    #     profile.save()
    #     new_user = auth.authenticate(username=username, password=password)
    #     if new_user is not None:
    #         auth.login(request, new_user)
    #         return HttpResponseRedirect('/accounts/profile')
    #     else:
    #         return HttpResponseRedirect('/accounts/login')
    
    # form = UserCreationForm()
    # return render_to_response("accounts/register.html", {
    #     'form': form,
    # }, context_instance=RequestContext(request))


def signup_organization(request):
    if request.method == 'POST':
        form = OrganizationSignUpForm(request.POST)
        if form.is_valid():
            return render_to_response('render.html', {'result': 'yes'})
        else:
            return render_to_response('render.html', {'result': 'no'})
            #organization = form.save()
    else:
        form = OrganizationSignUpForm()
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
