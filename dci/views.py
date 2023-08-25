from django.shortcuts import render, get_object_or_404
from dci.request_etp import buscar_etp, atualizar
from dci.models import EtpOnline, OesDci, OtsDCI, DciGerada
from dci.forms import DciForms
from django.http import HttpResponse
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa


def index(request):
    return render(request, "dci/index.html")


def formulario(request):

    if 'search' in request.GET:

        etp_nome = request.GET['search']

        etp_banco = EtpOnline.objects.filter(etp=etp_nome)

        if etp_banco.exists():

            dci = get_object_or_404(EtpOnline, etp=etp_nome)
            atualizar(dci.etp)
            oes = OesDci.objects.filter(etp_vinculada=dci.etp)
            ots = OtsDCI.objects.filter(etp_vinculada=dci.etp)
            contexto = {'dci': dci, 'oes': oes, 'ots': ots}
        else:
            if etp_nome != '':
                dci = buscar_etp(etp_nome)
                if dci != None:
                    oes = OesDci.objects.filter(etp_vinculada=dci.etp)
                    ots = OtsDCI.objects.filter(etp_vinculada=dci.etp)
                    contexto = {'dci': dci, 'oes': oes, 'ots': ots}
                else:
                    return render(request, 'dci/index.html')
            else:
                return render(request, 'dci/index.html')

        return render(request, 'dci/dci_formulario.html', contexto)
    else:
        return render(request, 'dci/index.html')


def selecionados(request):

    if request.method == 'POST':
        ots_select = request.POST.getlist('ots_select')
        oes_select = request.POST.getlist('oe_select')

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

        dci.gerar_lista_oes(oes_select)
        dci.gerar_lista_ots(ots_select)

        dci.save()

        lt_oes = dci.return_lista_oes()
        lt_ots = dci.return_lista_ots()

        etp = get_object_or_404(EtpOnline, etp=dci.etp_value)
        print(etp.etp)

        lista_oes = oes_selecionadas(lt_oes)
        lista_ots = ots_selecionadas(lt_ots)

        contexto = {'dci': dci, 'etp': etp, 'oes': lista_oes, 'ots': lista_ots}

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

                    contexto = buscar_dci(buscar)

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

    id_consulta = int(id_dci)

    dci_exist = DciGerada.objects.filter(id=id_consulta)

    if dci_exist.exists():

        contexto = buscar_dci(id_consulta)

        return render(request, 'dci/consulta_dci_etp.html', contexto)

    else:
        return render(request, 'dci/consulta_dci_etp.html')


def gerar_pdf(request, id_dci):

    template = get_template('dci/pdf_template.html')
    id_teste = id_dci
    dci_exist = DciGerada.objects.filter(id=id_teste)

    if dci_exist.exists():

        contexto = buscar_dci(id_teste)

    html = template.render(contexto)

    # Define a folha de estilo CSS
    css_path = 'setup/static/css/bootstrap.min.css'
    with open(css_path, 'r') as css_file:
        css = css_file.read()

    buffer = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html.encode('UTF-8')), buffer,
                         encoding='utf-8', css=css)

    if not pdf.err:
        response = HttpResponse(
            buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="dci.pdf"'
        return response
    else:
        return HttpResponse('Ocorreram erros ao gerar o PDF: %s' % html)


def teste_forms(request):
    forms = DciForms()
    return render(request, 'dci/teste_form.html', {'forms': forms})


def val_dci(id_dci):
    dci_banco = DciGerada.objects.all()
    res = False
    for item in dci_banco:
        if id_dci == item.id:
            res = True
            break

    return res


def oes_selecionadas(lt_oes):

    lista_oes = []

    for item in lt_oes:

        obj = OesDci.objects.filter(id=item)

        if obj.exists():

            obj = get_object_or_404(OesDci, id=item)
            lista_oes.append(obj)

    return lista_oes


def ots_selecionadas(lt_ots):

    lista_ots = []

    for item in lt_ots:

        obj = OtsDCI.objects.filter(id=item)

        if obj.exists():

            obj = get_object_or_404(OtsDCI, id=item)
            lista_ots.append(obj)

    return lista_ots


def buscar_dci(id_value):
    dci_value = get_object_or_404(DciGerada, id=id_value)
    lt_oes = dci_value.return_lista_oes()
    lt_ots = dci_value.return_lista_ots()
    etp = get_object_or_404(EtpOnline, etp=dci_value.etp_value)

    lista_oes = oes_selecionadas(lt_oes)
    lista_ots = ots_selecionadas(lt_ots)
    contexto = {'dci': dci_value, 'etp': etp,
                'oes': lista_oes, 'ots': lista_ots}

    return contexto
