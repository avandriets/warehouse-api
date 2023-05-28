from django.urls import (
    path,
    include,
)
from rest_framework.routers import DefaultRouter
from price import views


router = DefaultRouter()
router.register('', views.PriceTypesViewSet)

app_name = 'price'

urlpatterns = [
    path('', include(router.urls)),
]
