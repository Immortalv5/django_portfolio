from django.shortcuts import render, get_object_or_404
from .models import Projects

# Create your views here.
def index(request):
    return render(request, 'Projects/index.html')

def home(request):
    p = Projects.objects
    return render(request, 'Projects/home.html', {'projects':p})

def detail(request, p_id):
    project_detail = get_object_or_404(Projects, pk=p_id)
    return render(request, 'Projects/detail.html', {'project':project_detail})

def about(request):
    return render(request, 'Projects/about.html')
