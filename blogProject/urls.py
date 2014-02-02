from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blogProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^blog/test_view$', 'blog.views.test_view', name='home'),
	url(r'^blog/test_view2$', 'blog.views.test_view2'),
	url(r'^blog/list_blogs$', 'blog.views.list_blogs'),
	url(r'^blog/new_blog$', 'blog.views.new_blog'),
	url(r'^blog/edit_blog/(?P<blog_id>\d+)$', 'blog.views.edit_blog'),
    url(r'^admin/', include(admin.site.urls)),
)
