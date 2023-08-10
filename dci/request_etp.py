import requests
import json
from dci.models import DciOnline, OesDci


def buscar_etp(etp):

    base_url = "http://10.240.50.181:30009/api/etp/<etp>"

    etp = etp

    url = base_url.replace('<etp>', etp, 1)

    response = requests.get(url)

    if response.status_code == 200:

        data = json.loads(response.text)

        print(data['data_smtx_oe_oms'])

        dci = DciOnline(etp=data.get('etp', " "), titulo=data.get('titulo'), elaborador=data.get('elaborador', " "),
                        demanda=data.get('demanda', " "), motivador=data.get('motivador', " "),
                        vendor=data.get('vendor', " "), tipoEtp=data.get('tipoEtp', " "),
                        descri_etp=data.get('descricao_macro', " "), objetivo=data.get('objetivo', " "))

        dci.save()

        if len(data['data_smtx_oe_oms']) != 0:
            for item in data['data_smtx_oe_oms']:
                oe = OesDci(oe_id=item.get('id', ""), num_oe=item.get('numOE', ""), tipo_oe=item.get('TipoOE', ""),
                            status=item.get('Status', ""), descricao=item.get('Descricao', ""))
                oe.save()

        if len(data['data_smtx_oe_och']) != 0:
            for item in data['data_smtx_oe_och']:
                oe = OesDci(oe_id=item.get('id', ""), num_oe=item.get('numOE', ""), tipo_oe=item.get('TipoOE', ""),
                            status=item.get('Status', ""), descricao=item.get('Descricao', ""))
                oe.save()

        if len(data['data_smtx_oe_odu']) != 0:
            for item in data['data_smtx_oe_odu']:
                oe = OesDci(oe_id=item.get('id', ""), num_oe=item.get('numOE', ""), tipo_oe=item.get('TipoOE', ""),
                            status=item.get('Status', ""), descricao=item.get('Descricao', ""))
                oe.save()

        if len(data['data_smtx_oe_circuito']) != 0:
            for item in data['data_smtx_oe_circuito']:
                oe = OesDci(oe_id=item.get('id', ""), num_oe=item.get('numOE', ""), tipo_oe=item.get('TipoOE', ""),
                            status=item.get('Status', ""), descricao=item.get('Descricao', ""))
                oe.save()

        if len(data['data_smtx_oe_elemento']) != 0:
            for item in data['data_smtx_oe_elemento']:
                oe = OesDci(oe_id=item.get('id', ""), num_oe=item.get('numOE', ""), tipo_oe=item.get('TipoOE', ""),
                            status=item.get('Status', ""), descricao=item.get('Descricao', ""))
                oe.save()

        return dci
    else:

        print("Erro ao obter informações da ETP")
        return None
