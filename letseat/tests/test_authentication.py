from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse


def test_login_form(client):
    response = client.get(reverse('login'))
    assert response.status_code == 200
    assert 'form' in response.context_data
    assert type(response.context_data['form']) == AuthenticationForm
    assert 'next' in response.context_data
    assert response.context_data['next'] == ''
    assert '<title>Let\'s Eat</title>' in response.content
    assert 'Username' in response.content
    assert 'Password' in response.content
    assert 'Login' in response.content
    assert 'Register' in response.content
