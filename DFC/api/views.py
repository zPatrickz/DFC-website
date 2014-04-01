from django.shortcuts import render

# Create your views here.
import json
from photologue.models import Gallery
from django.http import HttpResponse

def gallery_list(request):
    # TODOS: check if authorized
    lst = list(Gallery.objects.values('id','title'))
    return HttpResponse(json.dumps(lst), content_type="application/json")
    
def gallery_photo_list(request,gal_id=None):
    # TODOS: check if authorized
    gal = Gallery.objects.get(id=gal_id)
    lst = []
    if not gal:
        return HttpResponse(json.dumps(lst), content_type="application/json")
    photos = gal.photos.all()
    lst = []
    for photo in photos:
        lst.append({"id":photo.id,"thumbnail":photo.get_photo_small_url(),"url":photo.image.url,"title":photo.title})
    return HttpResponse(json.dumps(lst), content_type="application/json")