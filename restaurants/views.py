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
        website = request.POST.get('website')
        logo = request.POST.get('logo')
        Restaurant.objects.create(created_by=request.user, modified_by= request.user, name=name,
                                  phone_number=phone_number, address=address, website=website, logo=logo)
        return HttpResponseRedirect(reverse('restaurants:index'))
    return TemplateResponse(request, 'new.html')
