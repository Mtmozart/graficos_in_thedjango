from django.urls import path

from .views import IndexView, DadosJSONView

urlpatte = [

    path('', IndexView.as_view(), name='index')
    path('dados/', DadosJSONView.as_view(), name='')
]