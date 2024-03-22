from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('user/', include("user.urls")),
                  path('cart/', include("cart.urls")),
                  path('product/', include("product.urls")),
                  path('', include("ecommerce.urls")),
              ] + [
                  re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
                  re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
              ] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
