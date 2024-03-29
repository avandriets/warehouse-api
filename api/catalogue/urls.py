from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from catalogue import views


router = DefaultRouter()
router.register('', views.CatalogueViewSet)

app_name = 'catalogue'

urlpatterns = [
    path('', include(router.urls)),
]
