from django.urls import path

from .views import contato, index, produto

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('produto/<int:pk>', produto, name='produto'),
]
