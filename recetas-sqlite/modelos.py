from abc import ABC, abstractmethod
from datetime import date

class ExcepcionReceta(Exception):
    pass

class ElementoMenu(ABC):
    @abstractmethod
    def mostrar_info(self) -> str:
        pass

class Ingrediente:
    def __init__(self, nome: str):
        self.__nome = nome
        self.id = None # for DB purpose

    def get_nome(self) -> str:
        return self.__nome

    @classmethod
    def crear_dende_string(cls, nome: str) -> "Ingrediente":
        return cls(nome)

    def __str__(self) -> str:
        return f"Ingrediente({self.__nome})"


class LinaIngrediente:
    def __init__(self, cantidade: float, unidade: str, ingrediente: Ingrediente):
        if not self.validar_unidade(unidade):
            raise ExcepcionReceta(f"Unidade non válida: {unidade}")
        self._cantidade = cantidade
        self._unidade = unidade
        self._ingrediente = ingrediente
        self.id = None # for DB purpose

    def get_ingrediente(self) -> Ingrediente:
        return self._ingrediente

    @staticmethod
    def validar_unidade(unidade: str) -> bool:
        unidades_validas = ['l', 'ml', 'g', 'kg', 'unidade', 'cucharada', 'pizca', 'taza']
        return unidade in unidades_validas

    def __str__(self) -> str:
        return f"{self._cantidade} {self._unidade} de {self._ingrediente.get_nome()}"


class Plato(ElementoMenu):
    def __init__(self, nome: str, tempada: str, preparacion: str, fotoUrl: str):
        self._nome = nome
        self._tempada = tempada
        self._preparacion = preparacion
        self._fotoUrl = fotoUrl
        self._ingredientes = []
        self.id = None # for DB purpose

    def engadirIngrediente(self, lina: LinaIngrediente):
        self._ingredientes.append(lina)

    def mostrar_info(self) -> str:
        return f"Plato: {self._nome} (Tempada: {self._tempada})\nPreparación: {self._preparacion}"

    def get_nome(self) -> str:
        return self._nome

    def __str__(self) -> str:
        ing_strs = [str(i) for i in self._ingredientes]
        return f"Plato: {self._nome} | Ingredientes: {', '.join(ing_strs)}"


class EntradaMenu:
    def __init__(self, data: date, momento: str, plato: Plato):
        self._data = data
        self._momento = momento
        self._plato = plato
        self.id = None # for DB purpose

    def __str__(self) -> str:
        return f"{self._data} ({self._momento}): {self._plato.get_nome()}"


class XestorMenu:
    def __init__(self):
        self.__entradas = []

    def xestionar(self, entrada: EntradaMenu):
        self.__entradas.append(entrada)

    def procurarPorSemana(self, inicio: date) -> list:
        # Simple implementation
        entradas_semanais = []
        for e in self.__entradas:
            if (e._data - inicio).days >= 0 and (e._data - inicio).days < 7:
                entradas_semanais.append(e)
        return entradas_semanais

    def procurarPorIngrediente(self, nome: str) -> list:
        atopados = []
        for e in self.__entradas:
            plato = e._plato
            for lina in plato._ingredientes:
                if lina.get_ingrediente().get_nome() == nome:
                    atopados.append(e)
                    break
        return atopados

    def __str__(self) -> str:
        res = "Menú Xestionado:\n"
        for i, e in enumerate(self.__entradas):
            res += f"  {i+1}. {e}\n"
        return res
