from django.contrib import auth
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views.decorators.http import require_GET, require_POST


def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home'))
    else:
        return HttpResponseRedirect(reverse('login_or_register'))


def login_or_register(request):
    return TemplateResponse(request, 'login_or_register.html')


@require_POST
def register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    confirm = request.POST.get('confirm')
    messages = []
    if password != confirm:
        # TODO: Better error notification
        # return TemplateResponse(request, 'login_or_register.html')
        messages.append('Passwords did not match!')
        return TemplateResponse(request, 'login_or_register.html', {'messages': messages, 'register_tab': True})
    User.objects.create_user(username, password=password)
    user = auth.authenticate(username=username, password=password)
    auth.login(request, user)
    return TemplateResponse(request, 'home.html')


@require_POST
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect(reverse('home'))
    else:
        return HttpResponseRedirect(reverse('login'))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def home(request):
    return TemplateResponse(request, 'home.html')
