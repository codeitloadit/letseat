from django.core.urlresolvers import reverse


def test_landing_page(client):
    response = client.get(reverse('home'))
    assert response.status_code == 200
    # assert '//maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css' in response.content
    # assert '//maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js' in response.content
    assert '//code.jquery.com/jquery-1.11.2.min.js' in response.content
    assert '<title>Pollar</title>' in response.content
    assert '<h1>Pollar</h1>' in response.content
    assert '">Login</a>' in response.content
    assert '">Sign Up</a>' in response.content
