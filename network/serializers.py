from rest_framework import serializers
from .models import Factory, Product, Retail, Individual


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    factory = FactorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class RetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    factory = FactorySerializer(read_only=True)

    class Meta:
        model = Retail
        fields = '__all__'


class IndividualSerializer(serializers.ModelSerializer):
    factory = FactorySerializer(read_only=True)
    products = ProductSerializer(read_only=True)

    class Meta:
        model = Individual
        fields = '__all__'

