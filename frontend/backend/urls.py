
m django.urls import path
from .views import ProductListView, OrderListView, OrderDetailView

urlpatterns = [
            path('products/', ProductListView.as_view(), name='product-list'),
                path('orders/', OrderListView.as_view(), name='order-list'),
                    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
                    ]

