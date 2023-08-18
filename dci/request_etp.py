import requests
import json
from dci.models import EtpOnline, OesDci, OtsDCI


def buscar_etp(etp):

    base_url = "http://10.240.50.181:30009/api/etp/<etp>"

    etp = etp

    url = base_url.replace('<etp>', etp, 1)

    response = requests.get(url)

    data = json.loads(response.text)

    if len(data) != 0:

        dci = EtpOnline(etp=data.get('etp', " "), titulo=data.get('titulo'),
                        elaborador=data.get('elaborador', " "), demanda=data.get('demanda', " "),
                        motivador=data.get('motivador', " "), vendor=data.get('vendor', " "),
                        tipoEtp=data.get('tipoEtp', " "), descri_etp=data.get('descricao_macro', " "),
                        objetivo=data.get('objetivo', " "))

        dci.save()

        gerar_oes(data['data_smtx_oe_oms'], dci.etp)
        gerar_oes(data['data_smtx_oe_och'], dci.etp)
        gerar_oes(data['data_smtx_oe_odu'], dci.etp)
        gerar_oes(data['data_smtx_oe_circuito'], dci.etp)
        gerar_oes(data['data_smtx_oe_elemento'], dci.etp)
        gerar_ots(data['data_smtx_ots'], dci.etp)

        dci.save()

        return dci
    else:

        print("Erro ao obter informações da ETP")
        return None


def gerar_oes(data, etp):
    if len(data) != 0:
        for item in data:
            oe = OesDci(etp_vinculada=etp, oe_id=item.get('id', ""),
                        num_oe=item.get('numOE', ""), tipo_oe=item.get('TipoOE', ""),
                        status=item.get('Status', ""), descricao=item.get('Descricao', ""))
            oe.save()
    else:
        print("Sem OES")


def gerar_ots(data, etp):
    if len(data) != 0:
        for item in data:
            ots = OtsDCI(etp_vinculada=etp, ots_id=item.get("idWDMOTS", ""), num_ots=item.get("ChaveOTS", ""),
                         sigla=item.get("Sigla", ""), proprietario=item.get("PropriedadeFibra", ""))
            ots.save()
    else:
        print("Sem OTS")
