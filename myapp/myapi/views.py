from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.password_validation import validate_password
from .serializers import CartSerializer, ItemSerializer, UserSerializer
from .models import User, Item, Cart
from .permissions import UserPermission, ItemPermission, CartPermission

# Create your views here.


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    http_method_names = ['get', 'post', 'delete', 'put']
    serializer_class = UserSerializer
    permission_classes = [
        UserPermission,
    ]

    def update(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            validate_password(request.data['password'])
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'msg': 'invalid password or user'})
        user.set_password(request.data['password'])
        user.save()
        return Response(status=status.HTTP_200_OK, data={'msg': 'Update success'})


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    http_method_names = ['get', 'post', 'delete', 'put']
    serializer_class = ItemSerializer
    permission_classes = [ItemPermission]


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    http_method_names = ['get', 'post', 'delete']
    serializer_class = CartSerializer
    permission_classes = [CartPermission]
