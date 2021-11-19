from django.shortcuts import render, redirect
from .models import Finder
from .forms import SearchForm


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
        for equip in equips:
            print(equip.id)
        
    return render(request, 'search.html', {'equips' : equips})


def delete_data (request, pk):
    equipment = Finder.objects.get(id=pk)
    if request.method == 'POST':
        equipment.delete()
        return redirect('/')

    context = {
        'equipment':equipment
    }
    return render(request, 'delete.html', context)

