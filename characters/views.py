from django.shortcuts import render
from characters.models import Characters

def heroes(request):
    form = Characters.objects.all()
    return render(request, 'heroes.html', {'form': form})

def hero_detail(request, id):
    if (id <= Characters.objects.order_by('-id').first().id) and id >= 1:    
        form = Characters.objects.get(id=id)
    else: 
        form = Characters.objects.get(id=1)
    return render(request, 'hero.html', {'form': form})