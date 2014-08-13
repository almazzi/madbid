from django.conf.urls import patterns, url
from bookmark.views import main_page, user_page, logout_page,register_page
import os.path
site_media = os.path.join(
    os.path.dirname(__file__), 'static'
)


urlpatterns = patterns('',
                       url(r'^$', main_page, name='main_page'),
                       url(r'^user/(\w+)/$', user_page),
                       url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
                       url(r'logout/$', logout_page, name='logout'),
                       url(r'static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': site_media}, name = 'static'),
                       url(r'^register/$', register_page)
                    )
