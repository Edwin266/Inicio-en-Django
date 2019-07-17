from django.http import HttpResponse
from django.shortcuts import render
from .models import Photo

# Create your views here.
#def home(request):
    #return HttpResponse('')
def post_list(request):
    posts = Photo.objects.order_by('created_at')
    return render(request, 'photos/post_list.html', {'posts' : posts})

