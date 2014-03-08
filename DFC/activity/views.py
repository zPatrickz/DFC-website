from django.shortcuts import render, get_object_or_404
from core.models import *
from activity.forms import *
from django.http import HttpResponseRedirect
#Views for Activity

def index(request):
    act_list = Activity.objects.order_by('-create_time')[:Activity.SHOW_ON_INDEXPAGE]
    return render(request,'activity/index.html',{'act_list':act_list})
    
def new_activity(request):
    if request.method == 'POST': # If the form has been submitted
        # Handle a submitted form
        form = ActivityForm(request.POST)
        if form.is_valid():
            # FAKE CREATE HERE, NEED MORE MODELS!!!
            Activity.create(name = form.cleaned_data['name'], organizations = Organization.objects.all())
            return HttpResponseRedirect('..')
    else:
        form = ActivityForm()
    return render(request,'activity/new.html',{'form':form})