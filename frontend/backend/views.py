
m rest_framework import generics
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer

class ProductListView(generics.ListCreateAPIView):
        queryset = Product.objects.all()
            serializer_class = ProductSerializer

            class OrderListView(generics.ListCreateAPIView):
                    queryset = Order.objects.all()
                        serializer_class = OrderSerializer

                        class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
                                queryset = Order.objects.all()
                                    serializer_class = OrderSerializer

