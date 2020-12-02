from django.shortcuts import render
#from django.http import HttpResponse

from .models import Resource

# Create your views here.
def index(request):
    return render(request,'api/index.html',{'':0})

def resource(request,resource_id):
    r = Resource.objects.get(pk=resource_id)
    context = r.serialize()
    context = {'context':context}
    return render(request,'api/details.html',context)

def all_resource(request):
    rs = Resource.objects.all()
    context = {r.id:r.serialize() for r in rs}
    context = {'context':context}
    return render(request,'api/resources.html',context)

def set_resource(request,resource):
    r = Resource(**resource)
    r.save()
