# Backlog inicial — aplicativo de kits

Todos os nomes, itens e situações deste documento são fictícios.

## História 1 — Consultar kits

**Como** pessoa responsável pelo estoque, **quero** visualizar os kits cadastrados, **para** localizar rapidamente os materiais disponíveis.

### Critérios de aceite

1. **Dado** que existam kits cadastrados, **quando** a pessoa abrir a lista de kits, **então** o sistema exibirá o nome e a identificação de cada kit.
2. **Dado** que não existam kits cadastrados, **quando** a pessoa abrir a lista, **então** o sistema exibirá uma mensagem informando que não há kits disponíveis, sem apresentar registros fictícios como reais.

## História 2 — Cadastrar item em um kit

**Como** pessoa responsável pelo estoque, **quero** adicionar um item a um kit, **para** manter a composição do kit atualizada.

### Critérios de aceite

1. **Dado** que o nome do item esteja preenchido e a quantidade seja maior que zero, **quando** a pessoa confirmar o cadastro, **então** o item será salvo e aparecerá na composição do kit.
2. **Dado** que a quantidade seja zero ou negativa, **quando** a pessoa tentar salvar o item, **então** o sistema recusará o cadastro, informará que a quantidade deve ser positiva e não gravará o item.

## História 3 — Consultar composição e quantidade

**Como** pessoa responsável pela montagem, **quero** consultar os itens e suas quantidades em um kit, **para** conferir se há material suficiente.

### Critérios de aceite

1. **Dado** que um kit possua itens cadastrados, **quando** a pessoa selecionar esse kit, **então** o sistema exibirá cada item e sua quantidade.
2. **Dado** que a identificação do kit não exista, **quando** a pessoa solicitar sua consulta, **então** o sistema recusará a operação e informará que o kit não foi encontrado.

## Definição de pronto da dupla

Uma história só poderá ser movida para **Pronto** quando:

1. Os critérios de aceite da história tiverem sido executados e seus resultados registrados.
2. Os testes automatizados relacionados estiverem passando (`python -m unittest -v`).
3. O código estiver revisado por outra pessoa da dupla, com a revisão registrada no histórico/descrição da tarefa.
4. O README ou a documentação da funcionalidade estiver atualizado com instruções suficientes para reproduzir a verificação.

## Quadro de trabalho

| A fazer | Fazendo | Revisão | Pronto |
|---|---|---|---|
| Implementar consulta de kits | — | — | — |
| Implementar cadastro de item | — | — | — |
| Implementar consulta da composição | — | — | — |

## Revezamento da dupla

- Pessoa A: escreve a primeira versão das histórias 1 e 2; Pessoa B revisa.
- Pessoa B: escreve a primeira versão da história 3; Pessoa A revisa.
- Após a revisão, a dupla registra ajustes e move cada cartão conforme o estado real.

**Nota:** os papéis acima são identificadores fictícios para demonstrar o revezamento. Substituam-nos pelos integrantes reais da dupla e registrem a troca realizada.
