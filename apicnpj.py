import re
import requests

def consulta_cnpj_razao(cnpj: str) -> str | None:
    cnpj = re.sub(r"\D", "", cnpj)
    url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}"
    r = requests.get(url, timeout=15)
    if r.status_code != 200:
        return None
    data = r.json()
    # alguns retornos usam "razao_social" / "nome" dependendo da fonte
    print(data.get("razao_social"))
    return data.get("razao_social") or data.get("nome")


