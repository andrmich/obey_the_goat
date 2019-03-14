from django.conf.urls import url, include
from lists import views as list_views
from lists import urls as list_urls

urlpatterns = [
    url(r'^$', list_views.home_page, name='home'),
    # url(r'^lists/new$', views.new_list, name='new_list'),
    # url(r'^lists/(\d)/$', views.view_list, name='view_list'),
    # url(r'^lists/(\d)/add_item$', views.add_item, name='add_item'),
    url(r'^lists/', include(list_urls)),
]
