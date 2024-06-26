from django.forms import model_to_dict
from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import WomenSerializer


# class WomenViewSet(viewsets.ModelViewSet):
#     # queryset = Women.objects.all()
#     serializer_class = WomenSerializer


class WomenAPIListPagination(PageNumberPagination):
    """
    Настройка пагинации
    """
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class WomenAPIList(generics.ListCreateAPIView):
    """
    Метод для чтения (по GET-запросу) и создания списка данных (по POST-запросу)
    """
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = WomenAPIListPagination

class WomenAPIUpdate(generics.UpdateAPIView):
    """
    Изменение записи по PUT- или PATCH-запросу
    """
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )

class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    """
    Удаляет определенную запись
    """
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly, )

# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     """
#     Чтение, изменение и добавление отдельной записи (GET-, PUT-, PATCH- и DELETE-запросы)
#     """
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
