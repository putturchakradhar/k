from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings
from .views import open_url_view

urlpatterns = [
    path('open_url/', open_url_view, name='open_url'),
    # Add other URL patterns if needed
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
