from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('getProfiles/', views.getProfiles, name='getProfiles'),
    path('create/', views.create, name='create'),
    path('create_profile/', views.create_profile, name='create_profile'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
