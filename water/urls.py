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
    path('clients/', clients_list),
    path('makers/', makers_list),
    path('orders/', order_list, name="order-list"),
    path('order/<int:id>/', order_info, name="order-info"),
    path('order/create/', order_create, name='order-create'),
    path('order/update/<int:id>/', order_update, name='order-update'),
    path('order/delete/<int:id>/', order_delete, name='order-delete'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
