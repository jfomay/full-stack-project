from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello World! This is a test')

def my_name(request):
    context = {'name': 'James'}
    return render(request, 'myapp/myapp.html', context)