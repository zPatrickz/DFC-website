from django.shortcuts import render, get_object_or_404, redirect
from document.models import Document
from document.forms import *
from django.http import HttpResponseRedirect,HttpResponse

def new(request):
    if request.method == 'POST': # If the form has been submitted
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save()
            return redirect('doc_detail',doc.id)
        else:
            print form.errors
    else:
        form = DocumentForm()
    return render(request,'document/document_new.html',{'form':form})

def detail(request,doc_id=None):
    doc = get_object_or_404(Document,id=doc_id)
    return render(request,'document/document_detail.html',{'doc':doc})
     