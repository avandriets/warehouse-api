from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from catalogue import views


router = DefaultRouter()
router.register('catalogue', views.CatalogueViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]
