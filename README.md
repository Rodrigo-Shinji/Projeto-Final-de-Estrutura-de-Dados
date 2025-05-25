# Documentação do Projeto: Sistema de Torneio de RPG

## 1. Informações sobre o Projeto

### Integrantes do Grupo:
* **Nome Completo:** Guilherme Dorce de Britto - **RA:** 1991866
* **Nome Completo:** Rodrigo Shinji Yamashita - **RA:** 2001443
* **Nome Completo:** Thiago Tsuyoshi Okada Aoki - **RA:** 2002282

### Temática do Projeto:
A ideia central do projeto é criar um campeonato de RPG textual, onde cada participante pode criar e gerenciar seus próprios personagens, formar times e, por fim, colocá-los em batalhas para decidir um vencedor.

Cada personagem criado possui um nome, um nível de força e um elemento próprio, alocado a ele dentre as opções pré-definidas (fogo, terra, luz, trevas, água, vento). A escolha de um elemento para cada personagem é obrigatória no momento de sua criação.

A incorporação dos elementos foi pensada para tornar as batalhas mais dinâmicas e estratégicas. No módulo de batalha, é possível escolher dois times para um confronto e, em seguida, selecionar um dos doze cenários pré-definidos. Cada cenário possui características únicas que afetam diretamente a força dos personagens com base em seus elementos. Por exemplo, o cenário "Vulcão" gera um bônus de ataque para personagens do tipo "Fogo" e "Terra", enquanto "Água" e "Vento" recebem penalidades, já que o cenário não os beneficia. Portanto, antes de iniciar a batalha, é essencial que os usuários pensem em composições de times que possam desfrutar da melhor eficiência em cada cenário.

## 2. Requisitos para Execução do Sistema

Para executar o sistema de Torneio de Personagens, você precisará ter o Python instalado em sua máquina. O projeto foi desenvolvido e testado com **Python 3.8+**.

### Dependências:
O projeto utiliza apenas bibliotecas padrão do Python (como `json`, `os`, `datetime`, `time`), não sendo necessário instalar nenhuma dependência externa.

### Estrutura de Pastas:
Certifique-se de que a estrutura de arquivos e pastas do projeto seja mantida conforme o original:

seu_projeto/
├── batalha.py
├── cenarios.py
├── elementos.py
├── historico.py
├── lista_encadeada.py
├── main.py
├── personagem.py
├── times.py
├── utils.py
└── data/
├── personagens.json (será criado automaticamente)
├── historico_batalhas.json (será criado automaticamente)
└── times.json (será criado automaticamente)

A pasta `data/` será criada automaticamente na primeira execução do sistema, caso não exista, e conterá os arquivos JSON para persistência dos dados.

### Como Executar:
1.  Navegue até o diretório raiz do projeto (onde o arquivo `main.py` está localizado) usando o terminal ou prompt de comando.
2.  Execute o arquivo `main.py` utilizando o interpretador Python:
    ```
    main.py
    ```
3.  O sistema apresentará um menu principal com opções para gerenciar personagens, gerenciar times, iniciar batalhas e visualizar o histórico.

## 3. Explicação Detalhada do Sistema

### Funcionalidades Principais:
* **Gerenciamento de Personagens:** Permite criar novos personagens com nome, força e elemento, além de visualizar, editar (nome, força, elemento) e excluir personagens existentes. Os dados são salvos para uso futuro.
* **Gerenciamento de Times:** Permite criar times, adicionar e remover personagens de times existentes, e visualizar a composição dos times.
* **Sistema de Batalha:** Simula o confronto entre dois times selecionados pelo usuário em um cenário escolhido. A força de cada personagem é ajustada por vantagens/desvantagens elementais e pelos efeitos do cenário. O time com a maior força total ajustada vence.
* **Histórico de Batalhas:** Mantém um registro das batalhas realizadas, indicando os times envolvidos e o vencedor, que pode ser consultado a qualquer momento.

### Estrutura Modular do Projeto:
O sistema é modular, dividido em vários arquivos Python, cada um responsável por uma parte específica da funcionalidade para facilitar a organização e manutenção do código:
* `main.py`: Ponto de entrada e orquestrador principal, lida com o menu e a interação do usuário.
* `personagem.py`: Funções para manipulação e persistência de dados de personagens.
* `lista_encadeada.py`: Implementação da estrutura de dados de Lista Encadeada.
* `times.py`: Funções para criação, gerenciamento e persistência de times, utilizando a Lista Encadeada.
* `elementos.py`: Definições das regras de elementos e cenários.
* `batalha.py`: Lógica de cálculo de força, aplicação de regras de vantagem/desvantagem e cenário, e determinação do vencedor da batalha.
* `historico.py`: Gerenciamento do registro e exibição das batalhas passadas.
* `utils.py`: Funções auxiliares para menus e validação de entrada de dados.

### Tabela de Vantagens e Desvantagens Elementais:

| Elemento Atacante | Vantagem contra (dano extra) | Desvantagem contra (dano reduzido) |
| :---------------- | :--------------------------- | :------------------------------- |
| Fogo              | Terra                        | Água                             |
| Água              | Fogo                         | Luz                              |
| Luz               | Fogo                         | Trevas                           |
| Vento             | Luz                          | Terra                            |
| Terra             | Vento                        | Fogo                             |
| Trevas            | Luz                          | Terra                            |

## 4. Justificativa da Escolha de Cada Estrutura de Dados

A escolha das estruturas de dados foi estratégica, visando otimizar o desempenho, a organização e a integridade dos dados, além de demonstrar o uso de diferentes paradigmas de coleções em Python.

### a) Dicionários (`dict`)
* **Uso:**
    * `personagens` (em `personagem.py`): Armazena dados de personagens (chave: nome do personagem).
    * `times` (em `times.py`): Mapeia o nome de cada time para sua `ListaEncadeada` de personagens.
    * `VANTAGENS`, `DESVANTAGENS`, `CENARIOS` (em `elementos.py`): Mapeiam elementos e cenários a suas respectivas regras e atributos.
    * Representação de Personagens: Cada personagem é um dicionário com `nome`, `forca` e `elemento`.
* **Justificativa:**
    * **Acesso Rápido por Chave:** Oferecem acesso $O(1)$ (tempo constante, em média) para buscar informações rapidamente por identificadores únicos (nomes de personagens, nomes de times, elementos).
    * **Associação de Dados Complexos:** Permitem associar identificadores textuais a conjuntos estruturados de dados (outros dicionários, listas, sets), ideal para representar entidades com múltiplos atributos.
    * **Flexibilidade para CRUD:** Por serem mutáveis, permitem o gerenciamento dinâmico de personagens e times (adição, remoção, modificação).

### b) Listas Encadeadas (`ListaEncadeada` personalizada)
* **Uso:**
    * Representar a coleção de personagens dentro de cada `time` (em `times.py`).
* **Tipo e Justificativa:**
    * A `ListaEncadeada` implementada é uma **lista encadeada simples**. Isso é evidente pelo atributo `self.proximo` em cada `Nodo`, que aponta apenas para o próximo elemento.
    * A escolha de uma lista encadeada simples foi suficiente para as operações necessárias (inserir personagens no final, remover por nome, listar todos). Não houve requisito para travessia reversa ou remoções complexas que justificassem a complexidade adicional de uma lista duplamente encadeada. O objetivo principal é a demonstração da compreensão e implementação de uma estrutura de dados fundamental.

### c) Sets (`set`)
* **Uso:**
    * `ELEMENTOS_VALIDOS` (em `personagem.py`): Armazena os elementos permitidos para os personagens.
    * `bonus` e `penalidade` dentro dos dicionários de `CENARIOS` (em `elementos.py`).
* **Justificativa:**
    * **Garantia de Unicidade:** Ideal para coleções onde cada item deve ser único, como a lista de elementos válidos ou os elementos afetados por bônus/penalidades de cenário, prevenindo duplicatas e mantendo a integridade.
    * **Verificação de Pertinência Otimizada:** Fornecem alta eficiência ($O(1)$ em média) para verificar se um elemento está presente na coleção. Isso é crucial para a validação rápida de entradas do usuário e para o cálculo eficiente da força dos personagens durante as batalhas (aplicação de bônus/penalidades de cenário).

### d) Tuplas (`tuple`)
* **Uso:**
    * Valores em `VANTAGENS` e `DESVANTAGENS` (em `elementos.py`): Coleções de elementos sobre os quais um elemento tem vantagem/desvantagem.
* **Justificativa:**
    * **Imutabilidade para Dados Fixos:** Tuplas são coleções imutáveis. Isso é perfeito para definir regras de jogo que não devem ser alteradas, como as relações de vantagem e desvantagem entre elementos, garantindo a consistência e a segurança dos dados do jogo.
    * **Eficiência e Semântica:** O uso de tuplas para esses dados fixos comunica claramente que eles são constantes, além de serem ligeiramente mais eficientes em termos de memória e processamento do que listas para essa finalidade.

### e) Listas Simples (`list`)
* **Uso:**
    * Retornos de funções que entregam coleções de dados (e.g., `listar_personagens()`, `obter_personagens_do_time()`, `carregar_historico()`).
    * Variáveis temporárias e parâmetros onde uma coleção mutável e ordenada é necessária (e.g., manipular o histórico de batalhas, ordenar elementos para exibição).
    * Formato de persistência JSON: Listas de dicionários para personagens e times.
* **Justificativa:**
    * **Coleções Ordenadas e Mutáveis Padrão:** São a estrutura de dados mais comum e flexível em Python para armazenar itens em uma sequência definida, permitindo fácil adição, remoção e modificação.
    * **Flexibilidade e Interoperabilidade:** Extremamente versáteis para manipular dados dinamicamente e compatíveis com o formato JSON, facilitando a persistência e o carregamento de dados.
    * **Suporte a Indexação:** Permitem acesso por índice numérico, essencial para a interação do usuário
