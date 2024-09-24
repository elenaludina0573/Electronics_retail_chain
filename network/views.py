from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from network.models import Factory, Individual, Retail, Product
from network.serializers import FactorySerializer, RetailSerializer, IndividualSerializer, ProductSerializer


class FactoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Factory model.
    """
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    filter_backends = DjangoFilterBackend
    filterset_fields = ['country']

    def has_object_permission(self, request):
        return request.user.is_staff or request.user.is_superuser


class RetailViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Retail model.
    """
    queryset = Retail.objects.all()
    serializer_class = RetailSerializer
    permission_classes = (IsAdminUser, IsAuthenticated)


class IndividualViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Individual model.
    """
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer
    permission_classes = (IsAdminUser, IsAuthenticated)


class ProductListAPIView(generics.ListAPIView):
    """
    API endpoint for listing all products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
