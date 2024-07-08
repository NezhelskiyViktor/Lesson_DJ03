from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_news, name='page_news'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
