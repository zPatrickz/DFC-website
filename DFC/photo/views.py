from django.shortcuts import render, get_object_or_404
from core.models import *
from photo.forms import *
from django.http import HttpResponseRedirect

def index(request):
    album_list = Album.objects.order_by('-create_time')[:Album.SHOW_ON_INDEXPAGE]
    return render(request,'photo/index.html',{'album_list':album_list})
    
def add_or_update_album(request,album_id=None):
    update = False
    if album_id:
        update = True
    if request.method == 'POST': # If the form has been submitted
        # Handle a submitted form
        if album_id:
            form = AlbumForm(request.POST, request.FILES,instance = Album.objects.get(id=album_id))
            if form.is_valid():
                # FAKE SAVE HERE, NEED MORE MODELS!!!
                form.save()
                return HttpResponseRedirect('')
        else:
            form = AlbumForm(request.POST, request.FILES)
            if form.is_valid():
                # FAKE SAVE HERE, NEED MORE MODELS!!!
                form.save()
                return HttpResponseRedirect('../..')
    elif album_id:
        #Handle an update form
        form = AlbumForm(instance = Album.objects.get(id=album_id))
    else:
        #Handle an empty form
        form = AlbumForm()
    return render(request,'photo/add_or_update_album.html',{'form':form,'update':update})

def view_album(request,album_id=None):
    album = get_object_or_404(Album,id=album_id)
    photo_list = Photo.objects.filter(album__exact = album).values('id','desc')
    return render(request,'photo/view_album_and_upload_photo.html',{'album':album,'photo_list':photo_list})
def view_photo(request,photo_id=None):  
    photo = get_object_or_404(Photo,id=photo_id)
    return render(request,'photo/view_photo.html',{'photo':photo})
    
def add_photo(request,album_id=None):
    album = get_object_or_404(Album,id=album_id)
    update = False
    if request.method == 'POST': # If the form has been submitted
        # Handle a submitted form
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            # FAKE SAVE HERE, NEED MORE MODELS!!!
            form.save()
            return HttpResponseRedirect('../../album/'+str(album.id))
    else:
        #Handle an empty form
        form = PhotoForm(initial={'album': album})
    return render(request,'photo/add_photo.html',{'form':form,'update':update})