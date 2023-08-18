from django.shortcuts import render, get_object_or_404
from dci.request_etp import buscar_etp
from dci.models import EtpOnline, OesDci, OtsDCI, DciGerada


def index(request):
    return render(request, "dci/index.html")


def formulario(request):

    if 'search' in request.GET:

        etp_nome = request.GET['search']

        etp_banco = EtpOnline.objects.filter(etp=etp_nome)

        if etp_banco.exists():

            dci = get_object_or_404(EtpOnline, etp=etp_nome)
            oes = OesDci.objects.filter(etp_vinculada=dci.etp)
            ots = OtsDCI.objects.filter(etp_vinculada=dci.etp)
            contexto = {'dci': dci, 'oes': oes, 'ots': ots}
        else:
            if etp_nome != '':
                dci = buscar_etp(etp_nome)
                oes = OesDci.objects.filter(etp_vinculada=dci.etp)
                ots = OtsDCI.objects.filter(etp_vinculada=dci.etp)
                contexto = {'dci': dci, 'oes': oes, 'ots': ots}
            else:
                return render(request, 'dci/index.html')

        return render(request, 'dci/dci_formulario.html', contexto)
    else:
        return render(request, 'dci/index.html')


def selecionados(request):

    if request.method == 'POST':
        ots_selecionadas = request.POST.getlist('ots_select')
        oes_selecionadas = request.POST.getlist('oe_select')

        etp_value = request.POST.get('input_etp_value')
        print(f"Teste de variavel{etp_value}")
        obv_atr = request.POST.get('obv_atributos')
        obv_oes = request.POST.get('obv_oes')
        obv_rede = request.POST.get('obv_rede_ext')
        topologia = request.POST.get('input_topo')
        link = request.POST.get('input_doc')
        obv_final = request.POST.get('obv_final')
        tipo_entrega = request.POST.get('input_tp_entrega')

        dci = DciGerada(etp_value=etp_value, obv_atr=obv_atr, obv_oes=obv_oes, obv_rede_ext=obv_rede,
                        topologia=topologia, link=link, obv_final=obv_final, tipo_entrega=tipo_entrega)

        dci.gerar_lista_oes(oes_selecionadas)
        dci.gerar_lista_ots(ots_selecionadas)

        dci.save()

        lt_oes = dci.return_lista_oes()
        lt_ots = dci.return_lista_ots()

        etp = get_object_or_404(EtpOnline, etp=dci.etp_value)
        print(etp.etp)
        oes = OesDci.objects.filter(etp_vinculada=etp.etp)
        ots = OtsDCI.objects.filter(etp_vinculada=etp.etp)
        contexto = {'dci': dci, 'etp': etp, 'oes': oes,
                    'ots': ots, 'lt_oes': lt_oes, 'lt_ots': lt_ots}

        return render(request, 'dci/dci_consulta.html', contexto)
    else:
        return render(request, 'dci/dci_consulta.html')


def dci(request):

    if 'buscar' in request.GET:
        buscar = request.GET.get('buscar')
        if buscar != '':
            if val_dci(int(buscar)):
                dci_exist = DciGerada.objects.filter(id=buscar)

                if dci_exist.exists():
                    print("Falhou")
                    dci_value = get_object_or_404(DciGerada, id=buscar)
                    lt_oes = dci_value.return_lista_oes()
                    lt_ots = dci_value.return_lista_ots()
                    etp = get_object_or_404(EtpOnline, etp=dci_value.etp_value)
                    oes = OesDci.objects.filter(etp_vinculada=etp.etp)
                    ots = OtsDCI.objects.filter(etp_vinculada=etp.etp)

                    contexto = {'dci': dci_value, 'etp': etp, 'oes': oes,
                                'ots': ots, 'lt_oes': lt_oes, 'lt_ots': lt_ots}

                    return render(request, 'dci/dci_consulta.html', contexto)
                else:
                    return render(request, 'dci/dci_consulta.html')
            else:
                return render(request, 'dci/dci_consulta.html')
        else:
            return render(request, 'dci/index.html')


def pesq_etp(request):
    return render(request, "dci/pesq_etp.html")


def lista_dci(request):

    if 'buscar' in request.GET:
        buscar = request.GET.get('buscar')

        dci_exist = DciGerada.objects.filter(etp_value=buscar)

        if dci_exist.exists():

            contexto = {'dci': dci_exist}

            return render(request, "dci/lista_dci.html", contexto)
        else:
            return render(request, "dci/lista_dci.html")


def consulta_dci_etp(request, id_dci):

    id_consulta = id_dci

    dci_exist = DciGerada.objects.filter(id=id_consulta)

    if dci_exist.exists():
        dci_value = get_object_or_404(DciGerada, id=id_consulta)
        lt_oes = dci_value.return_lista_oes()
        lt_ots = dci_value.return_lista_ots()
        etp = get_object_or_404(EtpOnline, etp=dci_value.etp_value)
        oes = OesDci.objects.filter(etp_vinculada=etp.etp)
        ots = OtsDCI.objects.filter(etp_vinculada=etp.etp)

        contexto = {'dci': dci_value, 'etp': etp, 'oes': oes,
                    'ots': ots, 'lt_oes': lt_oes, 'lt_ots': lt_ots}

        return render(request, 'dci/consulta_dci_etp.html', contexto)

    else:
        return render(request, 'dci/consulta_dci_etp.html')


def val_dci(id_dci):
    dci_banco = DciGerada.objects.all()
    res = False
    for item in dci_banco:
        if id_dci == item.id:
            res = True
            break

    return res
