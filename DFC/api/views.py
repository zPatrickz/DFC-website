from django.shortcuts import render

# Create your views here.
import json
from photologue.models import Gallery
from django.http import HttpResponse

def gallery_list(request):
    # api parameter category - category of the photo, must be specified, otherwise return empty list
    # 
    # TODO: check if authorized
    # TODO: restrict gallery list within category
    category = None
    if request.GET.get('category'):
        category = request.GET['category']
    if not category:
        return HttpResponse(json.dumps([]), content_type="application/json")
    lst = list(Gallery.objects.values('id','title'))
    return HttpResponse(json.dumps(lst), content_type="application/json")
    
def gallery_photo_list(request,gal_id=None):
    # TODO: check if authorized
    gal = Gallery.objects.get(id=gal_id)
    category = None
    if request.GET.get('category'):
        category = request.GET['category']
    if not gal or not category:
        return HttpResponse(json.dumps([]), content_type="application/json")
    photos = gal.photos.all()
    lst = []
    
    for photo in photos:
        lst.append({"id":photo.id,"small":photo.get_url(category,'small'),"medium":photo.get_url(category,'medium'),"large":photo.get_url(category,'large'),"title":photo.title})
            
    return HttpResponse(json.dumps(lst), content_type="application/json")