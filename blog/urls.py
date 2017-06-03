from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^about/$', views.TemplateView.as_view(template_name='blog/about.html'), name='about'),
    url(r'^contact/$', views.TemplateView.as_view(template_name='blog/contact.html'), name='contact'),

    # url(r'^archive/(?P<year>\d{4})/(?P<month>\d{1,2})/$', views.index, name='month_archive'),
    # url(r'^category/(?P<category>[-\w]+)/$', view=views.category, name='category'),
    url(r'^post/(?P<year>\d{4})/(?P<month>\d{2})/(?P<slug>[-\w]+)/$',
        views.PostDetail.as_view(), name='post'),
    url(r'^register/$',
        views.UserCreate.as_view(), name='register'),
    url(r'^login/$',
        views.LoginView.as_view(), name='login'),
    url(r'^new-post/$',
        views.NewPostView.as_view(), name='new-post'),

]
