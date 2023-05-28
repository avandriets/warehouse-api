from django.urls import (
    path,
    include,
)
from rest_framework.routers import DefaultRouter
from customers import views


router = DefaultRouter()
router.register('', views.CustomersViewSet)

app_name = 'customers'

urlpatterns = [
    path('', include(router.urls)),
]
