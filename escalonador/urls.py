from django.urls import path
from escalonador import views

urlpatterns = [
    path('', views.lista_pronto, name='lista_pronto'),
    path('criar_processo/', views.criar_processo, name='criar_processo'),
]