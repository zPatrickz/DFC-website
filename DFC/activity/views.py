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
    
def detail_member(request,act_id=None):
    activity = get_object_or_404(Activity,id=act_id)
    organizations = activity.organizations.all()
    places = activity.places.all()
    return render(request,'activity/activity_detail_member.html',{'act_id':act_id,'activity':activity,'organizations':organizations,'places':places})

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
    
def detail_settings(request,act_id=None,category='general'):
    if category == '':
        category = 'general'
    if request.method == 'POST': # If the form has been submitted
        # Handle a submitted form
        form = ActivityForm(request.POST, request.FILES,instance = get_object_or_404(Activity,id=act_id))
        if form.is_valid():
            # FAKE SAVE HERE, NEED MORE MODELS!!!
            form.save()
            #return HttpResponseRedirect('')
    else:
        #Handle an update form
        form = ActivityForm(instance = get_object_or_404(Activity,id=act_id))
    return render(request,'activity/activity_detail_settings.html',{'form':form,'act_id':act_id,'category':category})
    
def new(request):
    if request.method == 'POST': # If the form has been submitted
        form = ActivityForm(request.POST, request.FILES)
        if form.is_valid():
            act = form.save()
            from django.shortcuts import redirect
            return redirect('activity_complete_or_view',act.id)
        else:
            print form.errors
    else:
        form = ActivityForm()
    return render(request,'activity/activity_new.html',{'form':form})
    
def complete_or_view(request,act_id=None):
    return render(request,'activity/activity_complete_or_view.html',{'act_id':act_id})
    
