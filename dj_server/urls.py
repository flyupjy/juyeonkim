from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from work.views import MainPaintingView


urlpatterns = [
    path('', MainPaintingView.as_view(template_name='index.html'), name='index'),
    path('works/', include('work.urls')),
    path('exhibitions/', include('show.urls')),
    path('text/', TemplateView.as_view(template_name='text.html'), name='text'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', include('contact.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
