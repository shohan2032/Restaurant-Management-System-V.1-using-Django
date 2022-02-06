from .models import Owner_Panel,Food_Panel
from django.db.models import Q

def searchOwners(request):
    search_owner = ''
    
    if request.GET.get('search_owner'):
        search_owner = request.GET.get('search_owner')
        
    owners = Owner_Panel.objects.distinct().filter(
        Q(name__icontains=search_owner) |
        Q(gmail__icontains=search_owner) |
        Q(id__icontains=search_owner) |
        Q(number__icontains=search_owner)
    ).order_by('owner_priority_serial')
    return owners, search_owner


def searchfoods(request):
    search_food = ''
    
    if request.GET.get('search_food'):
        search_food = request.GET.get('search_food')
        
    foods = Food_Panel.objects.distinct().filter(
        Q(name__icontains=search_food) |
        Q(quantity__icontains=search_food) |
        Q(id__icontains=search_food) |
        Q(price__icontains=search_food)
    ).order_by('food_priority_serial')
    return foods, search_food