from rest_framework.serializers import HyperlinkedModelSerializer
from .models import User, Item, Cart


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'password', 'is_active', 'is_staff']


class ItemSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class CartSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
