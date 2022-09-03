from rest_framework.routers import DefaultRouter
from django.urls.conf import path, include
from django.conf import settings
from django.views.static import serve

from . import views

router = DefaultRouter()
router.register(prefix='users', viewset=views.UsersViewSet)
router.register(prefix='items', viewset=views.ItemViewSet)
router.register(prefix='carts', viewset=views.CartViewSet)
urlpatterns = [
    path(
        "api-auth/", include("rest_framework.urls")),
]

urlpatterns += router.urls
