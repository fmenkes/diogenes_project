from django.conf.urls import patterns, url

from diogenes import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^collection/$', views.collection, name='collection'),
        url(r'^about/$', views.about, name='about'),
        url(r'^add_book/$', views.add_book, name='add_book'),
        url(r'^delete_book/$', views.delete_book, name='delete_book'),
        url(r'^edit_book/(?P<book_slug>[\w\-]+)/$', views.edit_book, name='edit_book'),
        
)