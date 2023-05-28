from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from unitofmeasures import views


router = DefaultRouter()
router.register('', views.UoMViewSet)

app_name = 'unit_of_measures'

urlpatterns = [
    path('', include(router.urls)),
]
