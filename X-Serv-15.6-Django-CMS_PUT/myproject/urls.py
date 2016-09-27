from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^content/$', 'cms.views.getcontent'),
    url(r'^content/insert$', 'cms_put.views.insertcontent'),
    url (r'^content/(\d+)$', 'cms.views.searchcontent'),
    url(r'^admin/', include(admin.site.urls)),
    url (r'.*', 'cms.views.notfound'),
)
