from django.shortcuts import render, get_object_or_404
from core.models import *
from activity.forms import *
from django.http import HttpResponseRedirect
#Views for Activity

def index(request):
    act_list = Activity.objects.order_by('-create_time')[:Activity.SHOW_ON_INDEXPAGE]
    return render(request,'activity/index.html',{'act_list':act_list})
    
def add_or_update_activity(request,act_id=None):
    update = False
    if act_id:
        update = True
    if request.method == 'POST': # If the form has been submitted
        # Handle a submitted form
        if act_id:
            form = ActivityForm(request.POST, request.FILES,instance = Activity.objects.get(id=act_id))
            if form.is_valid():
                # FAKE SAVE HERE, NEED MORE MODELS!!!
                form.save()
                return HttpResponseRedirect('')
        else:
            form = ActivityForm(request.POST, request.FILES)
            if form.is_valid():
                # FAKE SAVE HERE, NEED MORE MODELS!!!
                form.save()
                return HttpResponseRedirect('..')
    elif act_id:
        #Handle an update form
        form = ActivityForm(instance = Activity.objects.get(id=act_id))
    else:
        #Handle an empty form
        form = ActivityForm()
    return render(request,'activity/add_or_update.html',{'form':form,'update':update})