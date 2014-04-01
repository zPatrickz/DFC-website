from django.conf import settings
from django.views.generic.dates import ArchiveIndexView, DateDetailView, DayArchiveView, MonthArchiveView, YearArchiveView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Photo, Gallery
from .forms import PhotoForm, GalleryForm
from django.shortcuts import render, get_object_or_404

# Number of galleries to display per page.
GALLERY_PAGINATE_BY = getattr(settings, 'PHOTOLOGUE_GALLERY_PAGINATE_BY', 20)

# Number of photos to display per page.
PHOTO_PAGINATE_BY = getattr(settings, 'PHOTOLOGUE_PHOTO_PAGINATE_BY', 20)

# Gallery views.
def gallery_detail(request,gal_id=None):
    gallery = get_object_or_404(Gallery,id=gal_id)
    photos = gallery.photos.all()
    return render(request,'photo/gallery_detail.html',{'object':gallery})
    
def gallery_new(request):
    if request.method == 'POST': # If the form has been submitted
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            gallery = form.save()
            from django.shortcuts import redirect
            return redirect('pl-gallery',gallery.id)
        else:
            pass
    else:
        form = GalleryForm()
    return render(request,'photo/gallery_new.html',{'form':form})


def photo_detail(request,ph_id=None):
    photo = get_object_or_404(Photo,id=ph_id)
    return render(request,'photo/photo_detail.html',{'object':photo})
    
def photo_new(request):
    if request.method == 'POST': # If the form has been submitted
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()
            from django.shortcuts import redirect
            return redirect('pl-photo',photo.id)
        else:
            pass
    else:
        form = PhotoForm()
    if request.GET['popup'] :
        return render(request,'photo/photo_new_simple.html',{'form':form})
    else:
        return render(request,'photo/photo_new.html',{'form':form})
    

'''class GalleryView(object):
    queryset = Gallery.objects.filter(is_public=True)


class GalleryListView(GalleryView, ListView):
    paginate_by = GALLERY_PAGINATE_BY


class GalleryDetailView(GalleryView, DetailView):
    slug_field = 'title_slug'


class GalleryDateView(GalleryView):
    date_field = 'date_added'
    allow_empty = True


class GalleryDateDetailView(GalleryDateView, DateDetailView):
    slug_field = 'title_slug'


class GalleryArchiveIndexView(GalleryDateView, ArchiveIndexView):
    pass


class GalleryDayArchiveView(GalleryDateView, DayArchiveView):
    pass


class GalleryMonthArchiveView(GalleryDateView, MonthArchiveView):
    pass


class GalleryYearArchiveView(GalleryDateView, YearArchiveView):
    pass

# Photo views.


class PhotoView(object):
    queryset = Photo.objects.filter(is_public=True)


class PhotoListView(PhotoView, ListView):
    paginate_by = PHOTO_PAGINATE_BY


class PhotoDetailView(PhotoView, DetailView):
    slug_field = 'title_slug'


class PhotoDateView(PhotoView):
    date_field = 'date_added'
    allow_empty = True


class PhotoDateDetailView(PhotoDateView, DateDetailView):
    slug_field = 'title_slug'


class PhotoArchiveIndexView(PhotoDateView, ArchiveIndexView):
    pass


class PhotoDayArchiveView(PhotoDateView, DayArchiveView):
    pass


class PhotoMonthArchiveView(PhotoDateView, MonthArchiveView):
    pass


class PhotoYearArchiveView(PhotoDateView, YearArchiveView):
    pass'''

