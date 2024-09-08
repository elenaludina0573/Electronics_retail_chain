from django.urls import path
from rest_framework.routers import DefaultRouter


from network.apps import NetworkConfig
from network.views import FactoryViewSet, ProductListAPIView, ProductRetrieveAPIView, ProductCreateAPIView, \
    ProductUpdateAPIView, ProductDestroyAPIView, RetailViewSet, IndividualViewSet

app_name = NetworkConfig.name
router = DefaultRouter()
router.register(r'factory', FactoryViewSet, basename='factory')
router.register(r'retail', RetailViewSet, basename='retail')
router.register(r'individual', IndividualViewSet, basename='individual')

urlpatterns = [
    path('product/', ProductListAPIView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product_retrieve'),
    path('product/create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateAPIView.as_view(), name='product_update'),
    path('product/<int:pk>/delete', ProductDestroyAPIView.as_view(), name='product_delete'),
] + router.urls
