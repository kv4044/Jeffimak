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


def initialize_db():
    if db.is_closed():
        db.connect()
        db.create_tables([Motor], safe=True)


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
