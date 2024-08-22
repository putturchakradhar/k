from django.contrib import admin
from django.urls import include, path
from opener.views import open_url_view  # Import your view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('opener.urls')),  # Include the app's URL patterns
    path('open_url/', open_url_view, name='open_url'),
]
