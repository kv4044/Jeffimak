from peewee import *

db = SqliteDatabase('motores.db')


class Motor(Model):
    nome = CharField()
    potencia = CharField()
    corrente_nominal = CharField()
    corrente_trabalho = CharField()
    rolamento = CharField()
    acoplamento = CharField()
    fixacao = CharField()

    class Meta:
        database = db


class Contador(Model):
    valor = IntegerField(default=1)

    class Meta:
        database = db


def initialize_db():
    if db.is_closed():
        db.connect()
    db.create_tables([Motor, Contador], safe=True)
    if Contador.select().count() == 0:
        Contador.create(valor=1)


def buscar_motor(nome_equipamento):
    try:
        motor = Motor.get(Motor.nome == nome_equipamento)
        return {
            'nome': motor.nome,
            'potencia': motor.potencia,
            'corrente_nominal': motor.corrente_nominal,
            'corrente_trabalho': motor.corrente_trabalho,
            'rolamento': motor.rolamento,
            'acoplamento': motor.acoplamento,
            'fixacao': motor.fixacao
        }
    except Motor.DoesNotExist:
        return None


def carregar_contador():
    if db.is_closed():
        db.connect()
    contador, created = Contador.get_or_create(id=1)
    return contador.valor


def salvar_contador(valor):
    if db.is_closed():
        db.connect()
    contador, created = Contador.get_or_create(id=1)
    contador.valor = valor
    contador.save()
