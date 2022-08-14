from django.urls import path
from . import views

urlpatterns = [
    path('qr-code/', views.qrCode),
]