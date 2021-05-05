from django.shortcuts import render
from .models import Projects

# Create your views here.
def index(request):
    projs = Projects.objects.all()
    return render(request,'index.html',{'projs':projs})