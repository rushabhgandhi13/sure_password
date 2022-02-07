from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.login, name='login1'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('service/<int:pk>/',views.service,name='service'),
    path('delete/<int:pk>/',views.delete,name='delete'),
    path('view_password/<int:pk>',views.view_password, name="view_password")
    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)