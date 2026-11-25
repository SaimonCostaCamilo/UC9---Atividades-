# A01 — Estação, código testado, backlog e arquitetura

Pasta de entrega da atividade A01 da UC09. Os dados de exemplo são fictícios.

## Arquivos

- `ambiente.md` — roteiro e registro da verificação do Python, SQLite e Tkinter.
- `diagnostico.py` — implementação de `itens_disponiveis`.
- `test_diagnostico.py` — quatro testes automatizados.
- `backlog.md` — histórias de usuário, critérios de aceite, definição de pronto e quadro.
- `arquitetura.md` — separação em camadas e decisão sobre SQLite local.

## Requisitos

- Python 3 instalado.
- Para executar `python -m sqlite3 -v`, é necessário Python 3.12 ou superior.
- Tkinter depende de estar disponível na instalação do Python e de um ambiente gráfico funcional.

## Executar

Abra o PowerShell nesta pasta:

```powershell
python --version
python diagnostico.py
python -m unittest -v
```

Também execute `diagnostico.py` e os testes pela IDE, usando o interpretador configurado nela. Compare `sys.executable` entre terminal e IDE; a versão pode ser igual mesmo quando os executáveis são diferentes.

## Resultado esperado do diagnóstico

```text
Limite 1 => ['Notebook', 'Cabo HDMI']
Limite 4 => ['Cabo HDMI']
Limite 1 => []
```

## Teste de fronteira: `>=` versus `>`

A função correta inclui registros cuja quantidade é exatamente igual ao limite. Para demonstrar isso, altere temporariamente `>=` para `>` em `diagnostico.py` e rode:

```powershell
python -m unittest -v
```

O teste `test_quantidade_igual_ao_limite_e_incluida` deverá falhar, pois o item Notebook tem quantidade 3 e o limite do teste também é 3. Depois, restaure `>=` e execute os testes novamente. Não entregue o código com a alteração proposital.

## Limite da evidência de ambiente

Os resultados reais da estação não podem ser inferidos nem simulados neste pacote. Preencha `ambiente.md` após executar os comandos no seu computador. Registre mensagens de erro literalmente, sem inventar resultados.
