from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView
from django.urls import reverse_lazy
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('social_django.urls', namespace='social')),
    path('robokassa/', include('robokassa.urls')),
    path('speaking_club/', include('speaking_clubs.urls')),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('', RedirectView.as_view(url=reverse_lazy('main'))),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
