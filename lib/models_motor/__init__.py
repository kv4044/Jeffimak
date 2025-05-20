from peewee import SqliteDatabase, Model, CharField, IntegerField
import os

# Caminho para o banco de dados SQLite
db_path = 'motores.db'
db = SqliteDatabase(db_path)


# ---------------------------
# MODELOS DO BANCO DE DADOS
# ---------------------------

class BaseModel(Model):
    class Meta:
        database = db


class Motor(BaseModel):
    nome = CharField()
    potencia = CharField()
    corrente_nominal = CharField()
    corrente_trabalho = CharField()
    rolamento = CharField()
    acoplamento = CharField()
    fixacao = CharField()


class Contador(BaseModel):
    id = IntegerField(primary_key=True)
    valor = IntegerField()


class Configuracoes(BaseModel):
    chave = CharField(unique=True)
    valor = CharField()


# ---------------------------
# FUNÇÕES DE INICIALIZAÇÃO
# ---------------------------

def initialize_db():
    if db.is_closed():
        db.connect()
    db.create_tables([Motor, Contador, Configuracoes], safe=True)
    if not Contador.select().where(Contador.id == 1).exists():
        Contador.create(id=1, valor=1)
    if not Configuracoes.select().where(Configuracoes.chave == "PastaPDF").exists():
        Configuracoes.create(chave="PastaPDF", valor="")
    db.close()


# ---------------------------
# FUNÇÕES DE CONTADOR
# ---------------------------

def carregar_contador():
    if db.is_closed():
        db.connect()
    valor = Contador.get_by_id(1).valor
    db.close()
    return valor


def salvar_contador(novo_valor):
    if db.is_closed():
        db.connect()
    contador = Contador.get_by_id(1)
    contador.valor = novo_valor
    contador.save()
    db.close()


# ---------------------------
# FUNÇÕES DE CONFIGURAÇÃO
# ---------------------------

def salvar_caminho_pasta(caminho):
    if db.is_closed():
        db.connect()
    config, created = Configuracoes.get_or_create(chave="PastaPDF")
    config.valor = caminho
    config.save()
    db.close()


def carregar_caminho_pasta():
    if db.is_closed():
        db.connect()
    try:
        config = Configuracoes.get(Configuracoes.chave == "PastaPDF")
        caminho = config.valor
    except Configuracoes.DoesNotExist:
        caminho = ""
    db.close()
    return caminho


# ---------------------------
# BUSCAR DADOS DO MOTOR
# ---------------------------

def buscar_motor(nome_equipamento):
    if db.is_closed():
        db.connect()
    try:
        motor = Motor.get(Motor.nome == nome_equipamento)
        resultado = {
            "nome": motor.nome,
            "potencia": motor.potencia,
            "corrente_nominal": motor.corrente_nominal,
            "corrente_trabalho": motor.corrente_trabalho,
            "rolamento": motor.rolamento,
            "acoplamento": motor.acoplamento,
            "fixacao": motor.fixacao
        }
    except Motor.DoesNotExist:
        resultado = None
    db.close()
    return resultado
