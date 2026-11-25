# Arquitetura — aplicativo desktop de kits

Todos os dados e exemplos são fictícios.

## 1. Distribuição das responsabilidades em camadas

| Responsabilidade | Camada | Justificativa |
|---|---|---|
| Mostrar mensagem de erro ao usuário | Apresentação | A interface comunica o resultado da operação de forma compreensível. |
| Recusar quantidade menor ou igual a zero | Domínio/serviço | É uma regra de negócio que deve ser testável sem abrir a janela e reutilizável por diferentes telas. |
| Executar `INSERT` na tabela `item` | Dados | A gravação SQL e a persistência pertencem ao componente responsável pelo banco. |
| Ler o texto digitado no campo quantidade | Apresentação | A leitura do conteúdo de um widget depende da interface gráfica. |
| Calcular o total de itens de um kit | Domínio/serviço | O cálculo representa uma regra/consulta do domínio e não deve depender de widgets. |
| Abrir e fechar a conexão com o banco | Dados | O gerenciamento da conexão é responsabilidade da infraestrutura de persistência. |

## 2. Decisão arquitetural

### Contexto

O aplicativo de kits será usado inicialmente em uma estação desktop, em um cenário didático, com poucos usuários e dados fictícios. A prioridade é permitir desenvolvimento, execução e testes locais com configuração simples.

### Decisão

Usar **SQLite em arquivo local**. A camada de dados ficará responsável por abrir a conexão, executar comandos parametrizados, confirmar transações e fechar a conexão. A camada de domínio/serviço receberá dados já interpretados e aplicará as regras de negócio. A apresentação cuidará dos campos, botões e mensagens.

### Alternativa descartada

Banco de dados em servidor, que permitiria acesso centralizado por várias estações, mas exigiria configurar e manter um serviço, rede, credenciais, permissões e rotinas de disponibilidade.

### Consequências

- **Positivas:** instalação simples, não exige servidor separado e facilita transportar um pequeno projeto didático.
- **Negativas:** o arquivo fica vinculado à estação/ao ambiente em que está armazenado; compartilhar o mesmo banco entre várias máquinas exige uma estratégia adicional. Também é necessário cuidar de cópias de segurança e evitar concorrência excessiva de gravações.
- **Evolução possível:** se o aplicativo passar a ser usado simultaneamente por várias estações, reavaliar a decisão e considerar um banco servidor.

## 3. Regras de separação

- A apresentação não deve conter SQL nem decidir regras de negócio.
- O domínio/serviço não deve importar componentes de Tkinter.
- A camada de dados não deve exibir caixas de diálogo; deve retornar dados ou propagar erros para a camada superior.
- Consultas SQL devem usar parâmetros (`?` no SQLite), nunca concatenação de dados recebidos do usuário.
