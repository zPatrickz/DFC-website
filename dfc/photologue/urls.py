from django.conf.urls import *
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from photologue.models import Gallery,Photo
from .views import photo_detail, photo_new, gallery_detail, gallery_new


urlpatterns = patterns('',

    #url(r'^gallery/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[\-\d\w]+)/$',
    #    GalleryDateDetailView.as_view(),
    #    name='pl-gallery-detail'),
    #url(r'^gallery/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$',
    #    GalleryDayArchiveView.as_view(),
    #    name='pl-gallery-archive-day'),
    #url(r'^gallery/(?P<year>\d{4})/(?P<month>[a-z]{3})/$',
    #    GalleryMonthArchiveView.as_view(),
    #    name='pl-gallery-archive-month'),
    #url(r'^gallery/(?P<year>\d{4})/$',
    #    GalleryYearArchiveView.as_view(),
    #    name='pl-gallery-archive-year'),
    url(r'^gallery/add/$', gallery_new,
            name='add-gallery'),
    #url(r'^gallery/$',
    #    GalleryArchiveIndexView.as_view(),
    #    name='pl-gallery-archive'),
    #url(r'^$',
    #    RedirectView.as_view(url=reverse_lazy('pl-gallery-archive')),
    #    name='pl-photologue-root'),
    url(r'^gallery/(?P<gal_id>\d+)/$', gallery_detail , name='pl-gallery'),
    #url(r'^gallery/page/(?P<page>[0-9]+)/$', GalleryListView.as_view(), name='pl-gallery-list'),

    #url(r'^photo/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[\-\d\w]+)/$',
    #    PhotoDateDetailView.as_view(),
    #    name='pl-photo-detail'),
    #url(r'^photo/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$',
    #    PhotoDayArchiveView.as_view(),
    #    name='pl-photo-archive-day'),
    #url(r'^photo/(?P<year>\d{4})/(?P<month>[a-z]{3})/$',
    #    PhotoMonthArchiveView.as_view(),
    #    name='pl-photo-archive-month'),
    #url(r'^photo/(?P<year>\d{4})/$',
    #    PhotoYearArchiveView.as_view(),
    #    name='pl-photo-archive-year'),
    url(r'^photo/add/$', photo_new,
            name='add-photo'),
    #url(r'^photo/$',
    #    PhotoArchiveIndexView.as_view(),
    #    name='pl-photo-archive'),
    

    url(r'^photo/(?P<ph_id>\d+)/$',
        photo_detail,
        name='pl-photo'),
    #url(r'^photo/page/(?P<page>[0-9]+)/$',
    #    PhotoListView.as_view(),
    #    name='pl-photo-list'),

)


