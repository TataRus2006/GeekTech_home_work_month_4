from django.contrib import admin
from django.urls import path
from clients.views import *
from core.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', contacts),
    path('about/', about),
    path('', products_list),
    path('makers/', makers_list),
    path('clients/', ClientListView.as_view(), name='clients'),
    path('orders/', OrderListView.as_view(), name="order-list"),
    path('order/create/', OrderCreateView.as_view(), name='order-create'),
    path('order/update/<int:pk>/', OrderUpdateView.as_view(), name='order-update'),
    path('order/delete/<int:pk>/', OrderDeleteView.as_view(), name='order-delete'),
    path('order/<int:pk>/', OrderInfoView.as_view(), name="order-info"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
