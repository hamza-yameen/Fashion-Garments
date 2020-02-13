from django.conf.urls import url
from .views import (
    ProductListView,
    Product_List_View,
    DetailListView,
    Detail_List_View,
    ProductFeatureListView,
    ProductFeatureDetailView,
    DetailSlugListView
)
app_name = 'product'

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='list'),
    #url(r'^feature/$', ProductFeatureListView.as_view()),
    #url(r'^feature/(?P<pk>\d+)/$', ProductFeatureDetailView.as_view()),
    #url(r'^product/$', Product_List_View),
    #url(r'^product-class/(?P<pk>\d+)/$', DetailListView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', DetailSlugListView.as_view(), name='detail'),
    #url(r'^product/(?P<pk>\d+)/$', Detail_List_View),
]
