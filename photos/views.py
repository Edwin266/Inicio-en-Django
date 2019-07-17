from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#def home(request):
    #return HttpResponse('')
def post_list(request):
    return render(request, 'photos/post_list.html', {})

