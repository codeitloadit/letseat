from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.response import TemplateResponse

from restaurants.models import Restaurant


def index(request):
    restaurants = Restaurant.objects.all()
    print restaurants
    return TemplateResponse(request, 'index.html', {'restaurants': restaurants})


def new(request):
    if request.method == 'POST':
        name = request.POST.get('restaurant_name')
        if not name:
            return TemplateResponse(request, 'new.html', {'messages': ['Name is a required field!']})
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        menu = request.POST.get('menu')
        logo = request.POST.get('logo')
        Restaurant.objects.create(created_by=request.user, modified_by= request.user, name=name.strip(),
                                  phone_number=phone_number, address=address, menu=menu, logo=logo)
        return HttpResponseRedirect(reverse('restaurants:index'))
    return TemplateResponse(request, 'new.html')


def edit(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    if request.method == 'POST':
        restaurant.phone_number = request.POST.get('phone_number')
        restaurant.address = request.POST.get('address')
        restaurant.menu = request.POST.get('menu')
        restaurant.logo = request.POST.get('logo')
        restaurant.save()
        return HttpResponseRedirect(reverse('restaurants:index'))
    return TemplateResponse(request, 'edit.html', {'restaurant': restaurant})


def delete(request, pk):
    Restaurant.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('restaurants:index'))
