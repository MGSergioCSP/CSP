from peewee import *
from abc import ABC, abstractmethod
from datetime import date

db = SqliteDatabase('recetas_peewee.db')

class ExcepcionReceta(Exception):
    pass

class BaseModel(Model):
    class Meta:
        database = db

class ElementoMenu:
    def mostrar_info(self) -> str:
        raise NotImplementedError("mostrar_info non implementado en ElementoMenu")

class Ingrediente(BaseModel):
    nome = CharField(unique=True)

    def get_nome(self) -> str:
        return self.nome

    @classmethod
    def crear_dende_string(cls, nome: str) -> "Ingrediente":
        ingrediente, created = cls.get_or_create(nome=nome)
        return ingrediente

    def __str__(self) -> str:
        return f"Ingrediente({self.nome})"

class Plato(BaseModel, ElementoMenu):
    nome = CharField()
    tempada = CharField(null=True)
    preparacion = TextField(null=True)
    fotoUrl = CharField(null=True)

    def engadirIngrediente(self, lina: "LinaIngrediente"):
        lina.plato = self
        lina.save()

    def mostrar_info(self) -> str:
        return f"Plato: {self.nome} (Tempada: {self.tempada})\nPreparación: {self.preparacion}"

    def get_nome(self) -> str:
        return self.nome

    def __str__(self) -> str:
        ing_strs = [str(i) for i in self.lina_ingredientes]
        return f"Plato: {self.nome} | Ingredientes: {', '.join(ing_strs)}"


class LinaIngrediente(BaseModel):
    plato = ForeignKeyField(Plato, backref='lina_ingredientes', null=True)
    ingrediente = ForeignKeyField(Ingrediente)
    cantidade = FloatField()
    unidade = CharField()

    def get_ingrediente(self) -> Ingrediente:
        return self.ingrediente

    @staticmethod
    def validar_unidade(unidade: str) -> bool:
        unidades_validas = ['l', 'ml', 'g', 'kg', 'unidade', 'cucharada', 'pizca', 'taza']
        return unidade in unidades_validas

    def save(self, *args, **kwargs):
        if not self.validar_unidade(self.unidade):
            raise ExcepcionReceta(f"Unidade non válida: {self.unidade}")
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.cantidade} {self.unidade} de {self.ingrediente.get_nome()}"


class EntradaMenu(BaseModel):
    data = DateField()
    momento = CharField()
    plato = ForeignKeyField(Plato, backref='entradas_menu')

    def __str__(self) -> str:
        return f"{self.data} ({self.momento}): {self.plato.get_nome()}"


class XestorMenu:
    def __init__(self):
        # A variable internal __entradas represents the tracked items during this session
        self.__entradas = []

    def xestionar(self, entrada: EntradaMenu):
        self.__entradas.append(entrada)
        entrada.save()

    def cargar_dende_base(self):
        self.__entradas = list(EntradaMenu.select())

    def procurarPorSemana(self, inicio: date) -> list:
        # DB level search if needed, here we use memory implementation as diagram specifies
        entradas_semanais = []
        for e in self.__entradas:
            if (e.data - inicio).days >= 0 and (e.data - inicio).days < 7:
                entradas_semanais.append(e)
        return entradas_semanais

    def procurarPorIngrediente(self, nome: str) -> list:
        atopados = []
        for e in self.__entradas:
            for lina in e.plato.lina_ingredientes:
                if lina.ingrediente.nome == nome:
                    atopados.append(e)
                    break
        return atopados

    def __str__(self) -> str:
        res = "Menú Xestionado:\n"
        for i, e in enumerate(self.__entradas):
            res += f"  {i+1}. {e}\n"
        return res

def inicializar_db():
    db.connect()
    db.create_tables([Ingrediente, Plato, LinaIngrediente, EntradaMenu])
