from base64 import standard_b64encode
import time
from celery import Celery
from httpx import post
from celery.contrib import rdb
from validate_docbr import CPF

app = Celery(broker="pyamqp://guest@localhost//")


@app.task(
    bind=True, default_retry_delay=3, max_retry=5, autoretry_for=(ValueError, Exception)
)
def ocr_documento(self, documento: str) -> str:
    try:
        with open(documento, "rb") as f:
            documento = f.read()

        image = standard_b64encode(documento).decode("utf-8")

        image_data = f"data:image/jpeg;base64,{image}"

        payload = {
            "base64Image": image_data,
            "apikey": "helloworld",
            "language": "por",
            "isOverlayRequired": False,
        }
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        time.sleep(10)
        response = post(
            "https://api.ocr.space/parse/image",
            data=payload,
            headers=headers,
            timeout=30,
        )
        if response.status_code == 403:
            return "Erro 403: Verifique sua API Key ou Headers."
        response.raise_for_status()

        if response.status_code == 200:
            resultado = response.json()

            texto_extraido = resultado["ParsedResults"][0]["ParsedText"]
            texto_ = extrair_cpf(texto_extraido)
            res = validar_cpf_no_governo.delay(texto_)
            print("texto", texto_)
            return res

    except ValueError as exc:
        raise self.retry(exc=exc)
    except Exception as exc:
        raise self.retry(exc=exc)


import re

def extrair_cpf(texto):

    padrao = r'([a-zA-Z0-9]{3}\.[a-zA-Z0-9]{3}\.[a-zA-Z0-9]{3}-[a-zA-Z0-9]{2})'
    
    match = re.search(padrao, texto)
    if match:
        cpf_sujo = match.group(1)

        cpf_limpo = cpf_sujo.lower().replace('o', '0').replace('.', '').replace('-', '')
        return cpf_limpo
    return None

@app.task(bind=True)
def validar_cpf_no_governo(self, cpf_input: str):
    # rdb.set_trace()
    cpf = CPF()
    if cpf.validate(cpf_input):
        return {"code": 200, "result": "Válido"}
    return {"code": 400, "result": "Inválido"}


@app.task
def ola_mundo():
    return "ola mundo"
