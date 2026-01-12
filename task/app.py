from tasks import ocr_documento, validar_cpf_no_governo

# ola_mundo.delay()

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str 
    telefone: str
    documento: str




def cadastrar(pessoa: Pessoa):
    response = ocr_documento.delay(
        pessoa.documento)

    
    print("Resultado:", response)

p = Pessoa(
    'Eduardo',
    '12345678978963',
    'img2.png'
)

cadastrar(p)



