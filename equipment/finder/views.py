from django.core.checks import messages
from django.shortcuts import render, redirect
from .models import Finder
from .forms import SearchForm
from django.contrib import messages

# Create your views here.
def homepage(request):
    context = {}
    equips = Finder.objects.all()
    form = SearchForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()
         
        return render(request, 'search.html', {'equips' : equips})

    context['form'] = form
        
    return render(request, 'home.html', context)

def search(request):
    equips = Finder.objects.all()
    if request.GET.get('q'):
        query = request.GET['q']
        equips = Finder.objects.filter(description__icontains=query)
        
        
    return render(request, 'search.html', {'equips' : equips})


