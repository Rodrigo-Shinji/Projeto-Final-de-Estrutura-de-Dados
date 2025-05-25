class Nodo:
    """
    Representa um nó (elemento) individual em uma Lista Encadeada.
    Cada nó armazena um 'personagem' (um dicionário) e uma referência
    para o 'próximo' nó na sequência.
    """
    def __init__(self, personagem):
        self.personagem = personagem  # O dado armazenado neste nó (um dicionário de personagem).
        self.proximo = None           # Um ponteiro para o próximo nó na lista (inicialmente None).

class ListaEncadeada:
    """
    Implementa uma estrutura de dados de Lista Encadeada simples para gerenciar personagens.
    Permite inserir, remover, listar, verificar a existência de um personagem e calcular a força total.
    """
    def __init__(self):
        self.inicio = None  # Referência para o primeiro nó da lista (inicialmente a lista está vazia).

    def inserir(self, personagem):
        """
        Insere um novo personagem no final da lista encadeada.

        Args:
            personagem (dict): O dicionário de dados do personagem a ser inserido.
        """
        novo = Nodo(personagem)  # Cria um novo nó com o personagem fornecido.
        if not self.inicio:      # Se a lista estiver vazia (primeiro nó é None),
            self.inicio = novo   # o novo nó se torna o primeiro.
        else:
            atual = self.inicio  # Começa do primeiro nó.
            # Percorre a lista até encontrar o último nó (aquele cujo 'proximo' é None).
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo # Adiciona o novo nó como o próximo do último nó.

    def remover(self, nome_personagem):
        """
        Remove um personagem da lista encadeada pelo seu nome.

        Args:
            nome_personagem (str): O nome do personagem a ser removido.

        Returns:
            bool: True se o personagem foi encontrado e removido, False caso contrário.
        """
        atual = self.inicio    # Começa do primeiro nó.
        anterior = None        # Mantém uma referência para o nó anterior ao 'atual'.

        while atual: # Percorre a lista enquanto houver nós.
            # Verifica se o nome do personagem no nó atual corresponde ao nome procurado.
            if atual.personagem["nome"] == nome_personagem:
                if anterior:     # Se o nó a ser removido NÃO é o primeiro.
                    # O nó anterior aponta para o nó seguinte ao 'atual', efetivamente pulando 'atual'.
                    anterior.proximo = atual.proximo
                else:            # Se o nó a ser removido É o primeiro.
                    # O início da lista é atualizado para o próximo nó.
                    self.inicio = atual.proximo
                return True      # Personagem removido com sucesso.
            anterior = atual     # Atualiza 'anterior' para o nó atual.
            atual = atual.proximo# Move para o próximo nó.
        return False             # Personagem não encontrado na lista.

    def listar(self):
        """
        Retorna uma lista Python comum contendo todos os dicionários de personagens
        armazenados na lista encadeada.

        Returns:
            list: Uma lista de dicionários de personagens.
        """
        personagens = []    # Lista vazia para armazenar os personagens.
        atual = self.inicio # Começa do primeiro nó.
        while atual:        # Percorre a lista.
            personagens.append(atual.personagem) # Adiciona o dicionário do personagem à lista.
            atual = atual.proximo                # Move para o próximo nó.
        return personagens  # Retorna a lista completa de personagens.

    def calcular_forca_total(self):
        """
        Calcula a soma da força de todos os personagens presentes na lista encadeada.

        Returns:
            int: A soma total da força de todos os personagens.
        """
        total = 0           # Inicializa o total da força em zero.
        atual = self.inicio # Começa do primeiro nó.
        while atual:        # Percorre a lista.
            total += atual.personagem["forca"] # Soma a força do personagem atual ao total.
            atual = atual.proximo              # Move para o próximo nó.
        return total        # Retorna o total da força.

    def contem(self, nome_personagem):
        """
        Verifica se um personagem com o nome fornecido está presente na lista encadeada.
        A comparação de nomes ignora espaços em branco extras e diferenças de maiúsculas/minúsculas.

        Args:
            nome_personagem (str): O nome do personagem a ser procurado.

        Returns:
            bool: True se o personagem for encontrado, False caso contrário.
        """
        nome_personagem = nome_personagem.strip().lower() # Normaliza o nome procurado.
        atual = self.inicio                               # Começa do primeiro nó.
        while atual:                                      # Percorre a lista.
            # Compara o nome do personagem no nó atual (normalizado) com o nome procurado (normalizado).
            if atual.personagem["nome"].strip().lower() == nome_personagem:
                return True # Personagem encontrado.
            atual = atual.proximo # Move para o próximo nó.
        return False          # Personagem não encontrado.

    @classmethod
    def from_list(cls, lista):
        """
        Método de classe (construtor alternativo) que cria uma nova ListaEncadeada
        a partir de uma lista Python comum de dicionários de personagens.

        Args:
            lista (list): Uma lista de dicionários, onde cada dicionário representa um personagem.

        Returns:
            ListaEncadeada: Uma nova instância de ListaEncadeada populada com os personagens da lista.
        """
        nova = cls()        # Cria uma nova instância de ListaEncadeada vazia.
        for item in lista:  # Itera sobre cada item (personagem) na lista de entrada.
            nova.inserir(item) # Insere cada personagem na nova lista encadeada.
        return nova         # Retorna a lista encadeada preenchida.