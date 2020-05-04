from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('comment/', include('comment.urls')),
    path('likes/', include('likes.urls')),
    path('user/', include('user.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),
    path('favicon.ico', serve, {'path': 'favicon.ico'}),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
