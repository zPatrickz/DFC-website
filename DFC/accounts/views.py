from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from django.core.urlresolvers import reverse
from django.http import Http404


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            _login(request, user.username, user.password)
            return HttpResponseRedirect(reverse('accounts.views.index'))
    else:
        form = UserCreationForm()
    return render_to_response("registration/register.html", {
        'form': form,
    }, context_instance=RequestContext(request))


def index(request):
    return render_to_response('index.html')


def _login(request, username, password):
    pass


def getprofile(request):
    if request.user.is_authenticated():

        return render_to_response('profile.html', {'form': request.user})
    else:
        raise Http404