from django.urls import path
from . import views

urlpatterns = [

    path("", views.index, name="index"),
    path("search", views.formulario, name="search"),
    path('selecionados', views.selecionados, name="selecionados"),
    path('historico', views.dci, name="historico"),
    path('pesq-etp', views.pesq_etp, name='pesq-etp'),
    path('lista-dci', views.lista_dci, name='lista-dci'),
    path('consulta-dci-etp/<id_dci>',
         views.consulta_dci_etp, name='consulta-dci-etp'),
]
