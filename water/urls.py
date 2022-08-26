from django.contrib import admin
from django.urls import path
from clients.views import clients_list
from django.conf import settings
from django.conf.urls.static import static
from core.views import contacts, about, products_list
from core.views import makers_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', contacts),
    path('about/', about),
    path('products/', products_list),
    path('clients/', clients_list),
    path('makers/', makers_list),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
