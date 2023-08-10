from django.shortcuts import render, get_object_or_404
from dci.request_etp import buscar_etp
from dci.models import DciOnline, OesDci


def index(request):
    return render(request, "dci/index.html")


def formulario(request):

    etp_nome = request.GET['search_result']

    etp_banco = DciOnline.objects.filter(etp=etp_nome)

    if etp_banco.exists():

        dci = get_object_or_404(DciOnline, etp=etp_nome)
        oes = OesDci.objects.filter(status="Concluida")
        oes = oes.filter(descricao__icontains=dci.titulo)
        print(dci.titulo)
        contexto = {'dci': dci, 'oes': oes}
    else:
        dci = buscar_etp(etp_nome)
        oes = OesDci.objects.filter(status="Concluida")
        oes = oes.filter(descricao__icontains=dci.titulo)
        contexto = {'dci': dci, 'oes': oes}

    return render(request, 'dci/dci_formulario.html', contexto)
