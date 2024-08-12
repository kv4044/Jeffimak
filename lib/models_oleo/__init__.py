from peewee import *

# Conectando ao banco de dados SQLite para óleos
db_oleos = SqliteDatabase('oleos.db')


# Definindo um modelo base para óleos
class BaseModel(Model):
    class Meta:
        database = db_oleos


# Definindo o modelo Oleo
class Oleo(BaseModel):
    nome = CharField(unique=True)
    total_nao_usado = FloatField(default=0)  # Total de litros não usados
    total_usado = FloatField(default=0)  # Total de litros usados


# Definindo o modelo Equipamento
class Equipamento(BaseModel):
    nome = CharField(unique=True)
    oleo = ForeignKeyField(Oleo, backref='equipamentos')  # Relaciona o equipamento com um tipo de óleo
    oleo_usado = FloatField(default=0)


# Função para inicializar o banco de dados de óleos
def inicializar_banco_oleos():
    db_oleos.connect()
    db_oleos.create_tables([Oleo, Equipamento], safe=True)

    # Adicionar óleos se não existirem com valores específicos
    oleos = [
        ("Oleo 46", 100, 0),
        ("Oleo 68", 1000, 0),
        ("Oleo 460", 100, 0)
    ]

    for nome, total_nao_usado, total_usado in oleos:
        if not Oleo.select().where(Oleo.nome == nome).exists():
            adicionar_oleo(nome, total_nao_usado, total_usado)

    # Adicionar equipamentos se não existirem
    equipamentos = [
        ("hidraulico 01 descascadeira", "Oleo 68", 0),
        ("hidraulico injetores 2 descascadeira", "Oleo 68", 0),
        # Adicione mais equipamentos conforme necessário
    ]

    for nome, oleo_nome, oleo_usado in equipamentos:
        oleo = Oleo.get(Oleo.nome == oleo_nome)
        if not Equipamento.select().where(Equipamento.nome == nome).exists():
            adicionar_equipamento(nome, oleo, oleo_usado)


# Função para fechar o banco de dados de óleos
def fechar_banco_oleos():
    db_oleos.close()


# Função para adicionar um novo óleo
def adicionar_oleo(nome, total_nao_usado, total_usado):
    Oleo.create(nome=nome, total_nao_usado=total_nao_usado, total_usado=total_usado)


# Função para adicionar um novo equipamento
def adicionar_equipamento(nome, oleo, oleo_usado):
    Equipamento.create(nome=nome, oleo=oleo, oleo_usado=oleo_usado)


# Função para atualizar os valores dos óleos
def atualizar_oleo(nome, usado_adicional):
    try:
        oleo = Oleo.get(Oleo.nome == nome)
        oleo.total_nao_usado -= usado_adicional
        oleo.total_usado += usado_adicional
        oleo.save()
    except Oleo.DoesNotExist:
        raise ValueError(f"O óleo '{nome}' não foi encontrado no banco de dados.")


# Função para reiniciar os valores dos óleos
def reiniciar_oleo(nome):
    try:
        oleo = Oleo.get(Oleo.nome == nome)
        if nome == "Oleo 68":
            oleo.total_nao_usado = 1000  # Valor inicial para Oleo 68
        else:
            oleo.total_nao_usado = 100  # Valor inicial para outros óleos
        oleo.total_usado = 0
        oleo.save()
    except Oleo.DoesNotExist:
        raise ValueError(f"O óleo '{nome}' não foi encontrado no banco de dados.")
