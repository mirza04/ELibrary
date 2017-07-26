from django.conf.urls import url, include
from django.contrib.auth.models import User, Group
from rest_framework import routers, serializers, viewsets
from .models import Book


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('imageId', 'isbn', 'bookName', 'author','description', 'page', 'publisher','rating','num_rating','isRated',
                  'numberOfCopys', 'MAX_COPYS')