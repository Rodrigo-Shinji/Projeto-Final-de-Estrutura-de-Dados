# Classe que representa um nodo (elemento) da lista encadeada,
# que contém um personagem e um ponteiro para o próximo nodo
class Nodo:
    def __init__(self, personagem):
        self.personagem = personagem  # dado armazenado no nodo (personagem, dict)
        self.proximo = None           # referência para o próximo nodo na lista

# Classe que implementa uma lista encadeada simples para armazenar personagens
class ListaEncadeada:
    def __init__(self):
        self.inicio = None  # referencia para o primeiro nodo da lista (inicialmente vazia)

    # Método para inserir um personagem no final da lista
    def inserir(self, personagem):
        novo = Nodo(personagem)  # cria um novo nodo com o personagem
        if not self.inicio:      # se a lista estiver vazia
            self.inicio = novo   # novo nodo vira o primeiro
        else:
            atual = self.inicio
            # percorre até o último nodo da lista
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo  # adiciona o novo nodo no final

    # Método para remover um personagem da lista pelo nome
    def remover(self, nome_personagem):
        atual = self.inicio
        anterior = None
        while atual:
            # verifica se o nodo atual tem o personagem com o nome procurado
            if atual.personagem["nome"] == nome_personagem:
                if anterior:             # se não for o primeiro nodo
                    anterior.proximo = atual.proximo  # pula o nodo atual, removendo-o
                else:
                    self.inicio = atual.proximo       # remove o primeiro nodo
                return True  # indica sucesso na remoção
            anterior = atual
            atual = atual.proximo
        return False  # personagem não encontrado

    # Método que retorna uma lista com todos os personagens da lista encadeada
    def listar(self):
        personagens = []
        atual = self.inicio
        while atual:
            personagens.append(atual.personagem)  # adiciona o personagem na lista
            atual = atual.proximo
        return personagens

    # Método que calcula a soma da força de todos os personagens na lista
    def calcular_forca_total(self):
        total = 0
        atual = self.inicio
        while atual:
            total += atual.personagem["forca"]  # acumula a força
            atual = atual.proximo
        return total

    # Método que verifica se um personagem com nome dado está na lista
    def contem(self, nome_personagem):
        nome_personagem = nome_personagem.strip().lower()
        atual = self.inicio
        while atual:
            # compara nomes ignorando espaços e maiúsculas/minúsculas
            if atual.personagem["nome"].strip().lower() == nome_personagem:
                return True  # personagem encontrado
            atual = atual.proximo
        return False  # personagem não encontrado

    # Método de classe para criar uma lista encadeada a partir de uma lista comum de personagens
    @classmethod
    def from_list(cls, lista):
        nova = cls()            # cria uma nova lista encadeada vazia
        for item in lista:
            nova.inserir(item)  # insere cada personagem da lista comum na lista encadeada
        return nova
