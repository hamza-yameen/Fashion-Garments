from django.contrib import admin
from django.conf.urls import url, include
from .views import home, contact, about
from accounts.views import login_page, register_page, guest_resgiste_view
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^login/$', login_page, name='login'),
    url(r'^register/$', register_page, name='register'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/guest/$', guest_resgiste_view, name='guest_register'),
    url(r'^about/$', about, name='about'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^cart/', include("carts.urls", namespace="cart")),
    url(r'^product/', include("product.urls", namespace="product")),
    url(r'^search/', include("search.urls", namespace="search")),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
