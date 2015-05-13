from django.contrib.auth import views


def login(request):
    template_response = views.login(request)
    # Do something with `template_response`
    return template_response