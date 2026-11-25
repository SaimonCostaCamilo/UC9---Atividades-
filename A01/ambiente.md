# A01 — Registro da estação de trabalho

> **Importante:** os resultados abaixo não foram inventados. Este documento é um modelo de evidência: execute os comandos no seu computador e substitua os campos pendentes pelos resultados observados. Não publique caminhos que contenham seu nome de usuário fora do ambiente da turma.

## 1. Verificações

| Verificação | Terminal | IDE |
|---|---|---|
| `python --version` |
| `sys.executable` | 
| `python -m sqlite3 -v` | 
| `python -m tkinter` | 

### Comandos para o terminal (PowerShell)

Execute um por vez, na pasta da prática:

```powershell
python --version
python -c "import sys; print(sys.executable)"
python -m sqlite3 -v
python -m tkinter
```

Feche a janela do Tkinter depois de confirmar que abriu. Se um comando falhar, copie a mensagem de erro para a seção de pendências.

### Verificação pela IDE

Crie/execute este trecho no interpretador configurado na IDE:

```python
import sys
print(sys.executable)
```

Compare o caminho completo com o exibido pelo terminal. A igualdade de versão, isoladamente, não comprova que é o mesmo interpretador: a evidência principal é o caminho de `sys.executable`.

## 2. Conclusão

- Versão do Python observada:| Python 3.12.6
- Versão do SQLite observada: | SQLite version 3.45.3
- Tkinter abriu: O sistema abre uma pequena interface gráfica 
- Terminal e IDE usam o mesmo executável: o Terminal criou este executável C:\Python312\python.exe

## 3. Pendências e mensagens de erro

Registre aqui a mensagem literal e a etapa em que ocorreu. Se não houver falhas, escreva “Nenhuma pendência observada”.

- Pendência 1: PENDENTE DE VERIFICAÇÃO.
- Mensagem de erro: PENDENTE DE VERIFICAÇÃO.

**Observação:** `python -m sqlite3 -v` está disponível a partir do Python 3.12. Se a versão instalada for anterior, registre essa limitação; não a apresente como falha do código da atividade.
