from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.page1, name='page1'),
    path('page2/', views.page2, name='page2'),
    path('page3/', views.page3, name='page3'),
    path('page4/', views.page4, name='page4'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
