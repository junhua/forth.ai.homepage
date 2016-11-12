# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from djoser import views

# from cmsauth.views import (
# 						ChangePasswordView,
# 						CreateViews,
# 						UsersView)

admin.autodiscover()

urlpatterns = [
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^select2/', include('django_select2.urls')),
]
# auth_urls = [
# 	url(r'^auth/login/$', views.LoginView.as_view(), name='login'),
# 	url(r'^auth/logout/$', views.LogoutView.as_view(), name='logout'),
# 	# reset password
# 	url(r'^auth/password/$', ChangePasswordView.as_view(), name='change_password'),
# 	url(r'^auth/register/$', CreateViews.as_view(), name='create'),
# 	url(r'^auth/users/$', UsersView.as_view(), name='users'),

# ]
# urlpatterns += auth_urls
urlpatterns += i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^', include('cms.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns
