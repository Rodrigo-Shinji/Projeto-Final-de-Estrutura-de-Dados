class Nodo:
    def __init__(self, personagem):
        self.personagem = personagem
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def inserir(self, personagem):
        novo = Nodo(personagem)
        if not self.inicio:
            self.inicio = novo
        else:
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo

    def remover(self, nome_personagem):
        atual = self.inicio
        anterior = None
        while atual:
            if atual.personagem["nome"] == nome_personagem:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self.inicio = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def listar(self):
        personagens = []
        atual = self.inicio
        while atual:
            personagens.append(atual.personagem)
            atual = atual.proximo
        return personagens

    def calcular_forca_total(self):
        total = 0
        atual = self.inicio
        while atual:
            total += atual.personagem["forca"]
            atual = atual.proximo
        return total

    def contem(self, nome_personagem):
        nome_personagem = nome_personagem.strip().lower()
        atual = self.inicio
        while atual:
            if atual.personagem["nome"].strip().lower() == nome_personagem:
                return True
            atual = atual.proximo
        return False

    @classmethod
    def from_list(cls, lista):
        nova = cls()
        for item in lista:
            nova.inserir(item)
        return nova