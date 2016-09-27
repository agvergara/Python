from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'cms.views.redirect'),
	url(r'^annotated/content/$', 'cms.views.getcontent'),
	url(r'^login/$', 'django.contrib.auth.views.login'),
	url(r'^accounts/profile/$', 'cms.views.redirect'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^annotated/content/insert/$', 'cms_put.views.getform'),
    url(r'^annotated/content/insert/form/$', 'cms_put.views.insertcontent'),
    url (r'^annotated/content/(\d+)$', 'cms.views.searchcontent'),
    url(r'^admin/', include(admin.site.urls)),
    url (r'^.*', 'cms.views.notfound'),
)
