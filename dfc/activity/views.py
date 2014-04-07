from django.shortcuts import render, get_object_or_404, redirect
from core.models import *
from activity.forms import *
from django.http import HttpResponseRedirect
#Views for Activity

def index(request):
    activities = Activity.objects.order_by('-create_time')[:Activity.SHOW_ON_INDEXPAGE]
    return render(request,'activity/activity_index.html',{'activities':activities})

def detail_album(request,act_id=None):
    activity = get_object_or_404(Activity,id=act_id)
    return render(request,'activity/activity_detail_album.html',{'activity':activity})
    
def detail_detail(request,act_id=None):
    activity = get_object_or_404(Activity,id=act_id)
    return render(request,'activity/activity_detail_detail.html',{'activity':activity})
    
def detail_discuss(request,act_id=None):
    activity = get_object_or_404(Activity,id=act_id)
    from core.forms import ActivityPostForm
    post_form = ActivityPostForm()
    return render(request,'activity/activity_detail_discuss.html',{'post_form':post_form,'activity':activity})
    
def detail_doc(request,act_id=None):
    activity = get_object_or_404(Activity,id=act_id)
    return render(request,'activity/activity_detail_doc.html',{'activity':activity})
    
def detail_member(request,act_id=None):
    activity = get_object_or_404(Activity,id=act_id)
    return render(request,'activity/activity_detail_member.html',{'activity':activity})

def detail_notice(request,act_id=None):
    activity = get_object_or_404(Activity,id=act_id)
    return render(request,'activity/activity_detail_notice.html',{'activity':activity})

def detail_post_new(request,act_id=None):
    from core.forms import ActivityPostForm
    if request.method == 'POST': # If the form has been submitted
        form = ActivityPostForm(request.POST, request.FILES)
        print request.POST['activity']
        print
        print
        print
        if form.is_valid():
            post = form.save()
            if post.category == 'PST':
                return redirect('activity_detail_post',act_id)
            elif post.category == 'DIS':
                return redirect('activity_detail_discuss',act_id)
        else:
            print form.errors
    return HttpResponse('')
    
def detail_post(request,act_id=None):
    activity = get_object_or_404(Activity,id=act_id)
    from core.forms import ActivityPostForm
    post_form = ActivityPostForm()
    return render(request,'activity/activity_detail_post.html',{'post_form':post_form,'activity':activity})
    
def detail_settings(request,act_id=None,category='general'):
    activity = get_object_or_404(Activity,id=act_id)
    if category == '':
        category = 'general'
    if request.method == 'POST': # If the form has been submitted
        # Handle a submitted form
        form = ActivityForm(request.POST, request.FILES,instance = activity)
        if form.is_valid():
            # FAKE SAVE HERE, NEED MORE MODELS!!!
            form.save()
            return HttpResponseRedirect('')
    else:
        #Handle an update form
        form = ActivityForm(instance = activity)
    return render(request,'activity/activity_detail_settings.html',{'form':form,'activity':activity,'category':category})
    
def new(request):
    if request.method == 'POST': # If the form has been submitted
        form = ActivityForm(request.POST, request.FILES)
        if form.is_valid():
            act = form.save()
            return redirect('activity_complete_or_view',act.id)
        else:
            print form.errors
    else:
        form = ActivityForm()
    return render(request,'activity/activity_new.html',{'form':form})
    
def complete_or_view(request,act_id=None):
    return render(request,'activity/activity_complete_or_view.html',{'act_id':act_id})
    
