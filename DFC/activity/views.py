from django.shortcuts import render, get_object_or_404
from core.models import *
from activity.forms import *
from django.http import HttpResponseRedirect
#Views for Activity

def index(request):
    activities = Activity.objects.order_by('-create_time')[:Activity.SHOW_ON_INDEXPAGE]
    return render(request,'activity/activity_index.html',{'activities':activities})

def detail_album(request,act_id=None):
    activity = get_object_or_404(Activity,id=act_id)
    organizations = activity.organizations.all()
    places = activity.places.all()
    return render(request,'activity/activity_detail_album.html',{'act_id':act_id,'activity':activity,'organizations':organizations,'places':places})
    
def detail_detail(request,act_id=None):
    activity = get_object_or_404(Activity,id=act_id)
    organizations = activity.organizations.all()
    places = activity.places.all()
    return render(request,'activity/activity_detail_detail.html',{'act_id':act_id,'activity':activity,'organizations':organizations,'places':places})
    
def detail_discuss(request,act_id=None):
    activity = get_object_or_404(Activity,id=act_id)
    organizations = activity.organizations.all()
    places = activity.places.all()
    return render(request,'activity/activity_detail_discuss.html',{'act_id':act_id,'activity':activity,'organizations':organizations,'places':places})
    
def detail_doc(request,act_id=None):
    activity = get_object_or_404(Activity,id=act_id)
    organizations = activity.organizations.all()
    places = activity.places.all()
    return render(request,'activity/activity_detail_doc.html',{'act_id':act_id,'activity':activity,'organizations':organizations,'places':places})

def detail_notice(request,act_id=None):
    activity = get_object_or_404(Activity,id=act_id)
    organizations = activity.organizations.all()
    places = activity.places.all()
    return render(request,'activity/activity_detail_notice.html',{'act_id':act_id,'activity':activity,'organizations':organizations,'places':places})

def detail_post(request,act_id=None):
    activity = get_object_or_404(Activity,id=act_id)
    organizations = activity.organizations.all()
    places = activity.places.all()
    return render(request,'activity/activity_detail_post.html',{'act_id':act_id,'activity':activity,'organizations':organizations,'places':places})



    
def new_or_update_activity(request,act_id=None,step='general'):
    update = False
    if act_id:
        update = True
    if request.method == 'POST': # If the form has been submitted
        # Handle a submitted form
        if act_id:
            form = ActivityForm(request.POST, request.FILES,instance = get_object_or_404(Activity,id=act_id))
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
    return render(request,'activity/activity_new_or_update.html',{'act_id':act_id,'update':update,'step':step})
    
