Documentação do Projeto: Sistema de Torneio de Personagens
1. Informações do Grupo
Nome Completo: [Nome Completo do Integrante 1] - RA: [RA do Integrante 1]
Nome Completo: [Nome Completo do Integrante 2] - RA: [RA do Integrante 2]
Nome Completo: [Nome Completo do Integrante 3] - RA: [RA do Integrante 3]
2. Requisitos para Execução do Sistema
Para executar o sistema de Torneio de Personagens, você precisará ter o Python instalado em sua máquina. O projeto foi desenvolvido e testado com Python 3.8+.

Dependências:
O projeto utiliza apenas bibliotecas padrão do Python (como json, os, datetime, time), não sendo necessário instalar nenhuma dependência externa (via pip, por exemplo).

Estrutura de Pastas:
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
└── utils.py (assumindo que as funções de menu e entrada estão aqui, se não, adapte)
└── data/
    ├── personagens.json (será criado automaticamente)
    ├── historico_batalhas.json (será criado automaticamente)
    └── times.json (será criado automaticamente)
A pasta data/ será criada automaticamente na primeira execução do sistema, caso não exista, e conterá os arquivos JSON para persistência dos dados.

Como Executar:

Navegue até o diretório raiz do projeto (onde o arquivo main.py está localizado) usando o terminal ou prompt de comando.
Execute o arquivo main.py utilizando o interpretador Python:
Bash

python main.py
O sistema apresentará um menu principal com opções para gerenciar personagens, gerenciar times, iniciar batalhas e visualizar o histórico.
3. Explicação do Sistema
O Sistema de Torneio de Personagens é uma aplicação de linha de comando que simula batalhas entre times de personagens. Ele permite aos usuários:

Cadastrar e Gerenciar Personagens: Criar, visualizar, editar e excluir personagens, definindo seu nome, força e elemento (fogo, terra, luz, trevas, água, vento). Os dados dos personagens são persistidos em um arquivo JSON.
Criar e Gerenciar Times: Agrupar personagens em times, adicionando ou removendo membros. Os times são gerenciados usando uma estrutura de dados de Lista Encadeada personalizada e também são persistidos em um arquivo JSON.
Realizar Batalhas: Simular confrontos entre dois times. Durante a batalha, a força total de cada time é calculada, levando em consideração:
Vantagens/Desvantagens Elementais: Personagens recebem bônus ou penalidades de força com base em seus elementos e nos elementos dos personagens do time inimigo.
Cenário: O cenário da batalha aplica bônus ou penalidades de força adicionais a personagens com elementos específicos.
Visualizar Histórico: Registrar e exibir o histórico de todas as batalhas realizadas, mostrando os times envolvidos e o vencedor.
Como o Sistema Funciona (Visão Geral):

O sistema é modular, dividido em vários arquivos Python, cada um responsável por uma parte específica da funcionalidade:

main.py: Ponto de entrada do programa. Contém o loop principal do menu e as funções para gerenciar a interação do usuário com os diferentes módulos.
personagem.py: Gerencia as operações CRUD (Criar, Ler, Atualizar, Deletar) de personagens. Armazena personagens em um dicionário em memória e persiste esses dados em personagens.json.
lista_encadeada.py: Implementa uma estrutura de dados de Lista Encadeada genérica, utilizada para armazenar os personagens dentro de cada time.
times.py: Gerencia as operações CRUD de times. Utiliza a ListaEncadeada para cada time e persiste os dados em times.json. É responsável por adicionar/remover personagens de times.
elementos.py: Define as regras de vantagem e desvantagem elementais, bem como as características dos cenários de batalha, utilizando estruturas de dados imutáveis (tuplas e sets) para garantir a consistência desses dados.
batalha.py: Contém a lógica central da simulação de batalha, incluindo o cálculo de força ajustada com base em elementos e cenários, e a determinação do vencedor.
historico.py: Registra o resultado de cada batalha em historico_batalhas.json e permite a visualização do histórico.
utils.py (assumido): Contém funções auxiliares para exibir menus e tratar entradas de usuário, garantindo a validação dos dados.
4. Justificativa da Escolha de Cada Estrutura de Dados
A escolha das estruturas de dados foi feita visando otimizar o desempenho, a organização e a integridade dos dados, considerando os requisitos do sistema.

a) Dicionários (dict)
Uso:
personagens (em personagem.py): Armazena os dados de todos os personagens cadastrados, onde a chave é o nome do personagem e o valor é um dicionário contendo sua força e elemento.
times (em times.py): Mapeia o nome de cada time para uma instância de ListaEncadeada contendo seus personagens.
VANTAGENS, DESVANTAGENS (em elementos.py): Mapeiam um elemento a uma coleção de elementos sobre os quais ele tem vantagem ou desvantagem.
CENARIOS (em elementos.py): Mapeiam o nome de um cenário a um dicionário com suas características (bônus/penalidades de elemento e valores).
Representação de Personagens: Cada personagem é um dicionário com chaves como "nome", "forca" e "elemento".
Justificativa:
Acesso Rápido por Chave: Dicionários oferecem acesso O(1) (tempo constante, em média) aos valores através de suas chaves. Isso é ideal para buscar personagens pelo nome, times pelo nome, ou consultar as regras de vantagens/desvantagens e cenários.
Associação de Dados: Permitem associar nomes (strings) a objetos ou coleções de dados complexos (outros dicionários, listas ou instâncias de classes), o que é perfeito para representar entidades com múltiplos atributos.
Flexibilidade: São mutáveis, permitindo adicionar, remover ou modificar entradas dinamicamente, o que é essencial para o cadastro e gerenciamento de personagens e times.
b) Listas Encadeadas (ListaEncadeada personalizada)
Uso:
Representar a coleção de personagens dentro de cada time (em times.py).
Justificativa:
Aprendizado e Implementação de Estrutura Customizada: A escolha de uma lista encadeada, em vez de uma lista padrão do Python, demonstra a capacidade de implementar estruturas de dados fundamentais.
Inserção/Remoção Eficientes (teórica): Em uma lista encadeada, inserções e remoções no meio da lista (uma vez que o nó anterior é encontrado) podem ser O(1), diferente de listas padrão que podem exigir realocação e deslocamento de elementos. Embora para listas pequenas a diferença seja desprezível, para grandes volumes de dados onde inserções/remoções frequentes ocorrem no meio da coleção, ela pode ser mais eficiente. No contexto deste projeto, onde os times não devem ser excessivamente grandes, a escolha visa mais a demonstração do conhecimento em estruturas de dados.
Consumo de Memória (para alguns casos): Cada nó ocupa apenas o espaço do dado e um ponteiro, o que pode ser mais eficiente que listas dinâmicas que pré-alocam memória excessiva.
c) Sets (set)
Uso:
ELEMENTOS_VALIDOS (em personagem.py): Armazena os elementos permitidos para os personagens.
bonus e penalidade dentro dos dicionários de CENARIOS (em elementos.py).
Justificativa:
Unicidade Garantida: Sets armazenam apenas itens únicos. Isso é ideal para ELEMENTOS_VALIDOS, garantindo que não haja elementos duplicados. Da mesma forma, para os elementos de bônus e penalidade em cenários, um set garante que não haverá entradas repetidas sem sentido.
Verificação de Pertinência Rápida (in operador): Sets oferecem verificação de pertinência (se um item está no conjunto) com complexidade O(1) em média, o que é muito eficiente. Isso é crucial para verificar se um elemento é válido ou se um personagem se beneficia/penaliza em um cenário.
Imutabilidade Semântica: Embora o set em si seja mutável, o uso de sets para essas coleções fixas de elementos reforça a ideia de que a ordem não importa e que a composição é um "conjunto" de características, não uma sequência.
d) Tuplas (tuple)
Uso:
Valores em VANTAGENS e DESVANTAGENS (em elementos.py): As coleções de elementos sobre os quais um elemento tem vantagem/desvantagem são agora tuplas (ex: ("terra",)).
Justificativa:
Imutabilidade: Tuplas são coleções ordenadas e imutáveis. Uma vez criadas, seus elementos não podem ser alterados. Isso é perfeito para dados fixos como as regras de vantagem e desvantagem entre elementos, garantindo que essas regras não sejam acidentalmente modificadas durante a execução do programa.
Eficiência de Memória: Tuplas geralmente consomem menos memória do que listas para a mesma quantidade de dados, pois não precisam de espaço para operações de crescimento ou encolhimento.
Coleção de Dados Relacionados: Embora conjuntos pudessem ser usados aqui, tuplas foram escolhidas para demonstrar um uso de estrutura de dados imutável para dados fixos. Para coleções de um único item, a vírgula ("fogo",) é necessária para que o Python a reconheça como uma tupla.
e) Listas Simples (list)
Uso:
Resultados de funções como listar_personagens(), obter_personagens_do_time(), carregar_historico(), que retornam coleções de dados.
Parâmetros e variáveis temporárias em diversas funções, onde uma coleção mutável e ordenada é necessária para processamento.
No módulo historico.py, o histórico de batalhas é carregado e manipulado como uma lista de dicionários antes de ser salvo.
Temporariamente, na função selecionar_elemento() e editar_personagem() no main.py e personagem.py, para ordenar e indexar os elementos válidos (que são armazenados em um set).
As listas de personagens salvas dentro do JSON de times.json e personagens.json são listas de dicionários.
Justificativa:
Coleções Ordenadas e Mutáveis: Listas são ideais para armazenar coleções de itens onde a ordem de inserção é importante (como a ordem em que os personagens são listados para o usuário ou o histórico de batalhas) e onde os itens podem ser adicionados, removidos ou modificados após a criação da lista.
Flexibilidade: Permitem armazenar itens de diferentes tipos (embora neste projeto sejam predominantemente dicionários) e são fáceis de iterar.
Padrão para Retorno de Coleções: São a estrutura de dados padrão em Python para retornar múltiplas ocorrências de um tipo de dado, facilitando a manipulação subsequente (ex: for item in lista:).
Interoperabilidade com JSON: O formato JSON mapeia naturalmente para listas e dicionários em Python, tornando as operações de serialização e desserialização (json.load, json.dump) diretas e eficientes para a persistência de dados.
Suporte a Indexação: Permitem o acesso a elementos por índice numérico (ex: minha_lista[0]), o que é útil quando a ordem e a posição são relevantes (como na seleção de opções por número em menus).
