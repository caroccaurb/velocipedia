"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pagina import views as pagina_views
from paginapp import views as paginapp_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', pagina_views.index, name='index'),
    path('bicicleta', paginapp_views.bicicleta, name='bicicleta'),
    path('neumatico', paginapp_views.neumatico, name='neumatico'),
    path('frenos', paginapp_views.frenos, name='frenos'),
    path('tecnico', pagina_views.tecnico, name='tecnico'),
    path('login', pagina_views.login, name='login'),
    path('recuperar-contraseña', pagina_views.recuperar_contraseña, name='recuperar-contraseña'),
    path('registrar', pagina_views.registrar, name='registrar'),
    path('admin/', admin.site.urls),
    path('cuentas/', include('django.contrib.auth.urls')),
    path('mi-cuenta/', pagina_views.mi_cuenta, name='mi-cuenta'),
    path('carrito', pagina_views.carrito, name='carrito'),
    path('agregar/<int:producto_id>/', pagina_views.agregar_producto, name='agregar'),
    path('agregar_otro/<int:producto_id>/', pagina_views.agregar_otro_producto, name="agregar_otro"),
    path('eliminar/<int:producto_id>/', pagina_views.eliminar_producto, name='eliminar'),
    path('restar/<int:producto_id>/', pagina_views.restar_producto, name='restar'),
    path('limpiar/', pagina_views.limpiar_carrito, name='limpiar'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)