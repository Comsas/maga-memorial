from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.api_views import TemoignageViewset

router = DefaultRouter()
router.register('temoignages', TemoignageViewset, basename='temoignages')

urlpatterns = []

urlpatterns += router.urls
