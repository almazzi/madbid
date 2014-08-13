from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import render_to_response
from bookmark.forms import RegistrationForm


def main_page(request):
    return render_to_response('bookmark/main_page.html', {'user': request.user})

def user_page(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404('Requested user not found.')
    bookmarks = user.bookmark_set.all()
    template = get_template('bookmark/user_page.html')
    variables = Context({
    'username': username,
    'bookmarks': bookmarks
    })
    output = template.render(variables)
    return HttpResponse(output)


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/django_bookmarks/')


def register_page(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            email=form.cleaned_data['email'],
                                            password=form.cleaned_data['password1'],
                                            )
            return HttpResponseRedirect('/django_bookmarks/')
    else:
        form = RegistrationForm()
        variables = RequestContext(request, {'form': form})
    return render_to_response(
            'registration/register.html',
            variables)


# Create your views here.
