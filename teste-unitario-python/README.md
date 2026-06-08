
## Uso de IA para geração de cenários de teste

  

### Função escolhida

  

`multiplicar(a, b)`

  

### Prompt utilizado

  

```text
    Atue como um professor de Teste de Software.

    

    Tenho a seguinte função Python:


    def multiplicar(a, b):
        """Retorna a multiplicação de dois números."""
        return a * b
    

    Quero criar testes unitários usando unittest.

    

    Liste pelo menos 6 cenários de teste para essa função.

    

    Para cada cenário, informe:

    - nome do cenário;

    - entrada;

    - resultado esperado;

    - tipo do cenário: caso normal, caso de borda ou caso de erro.

    

    Não gere código ainda.
```


### Resposta do Prompt
    ### Cenário 1 — Multiplicação de inteiros positivos

    | Campo | Valor |
    |-------|-------|
    | **Nome** | `test_multiplicar_inteiros_positivos` |
    | **Entrada** | `a = 3`, `b = 4` |
    | **Resultado esperado** | `12` |
    | **Tipo** | Caso normal |

    Valida o comportamento básico da função com números inteiros positivos.

    ---

    ### Cenário 2 — Multiplicação por zero

    | Campo | Valor |
    |-------|-------|
    | **Nome** | `test_multiplicar_por_zero` |
    | **Entrada** | `a = 7`, `b = 0` |
    | **Resultado esperado** | `0` |
    | **Tipo** | Caso de borda |

    Zero é um valor limite: qualquer número multiplicado por zero deve resultar em zero.

    ---

    ### Cenário 3 — Multiplicação de número positivo por negativo

    | Campo | Valor |
    |-------|-------|
    | **Nome** | `test_multiplicar_positivo_por_negativo` |
    | **Entrada** | `a = 5`, `b = -3` |
    | **Resultado esperado** | `-15` |
    | **Tipo** | Caso normal |

    Garante que o sinal do resultado está correto quando um dos operandos é negativo.

    ---

    ### Cenário 4 — Multiplicação de dois números negativos

    | Campo | Valor |
    |-------|-------|
    | **Nome** | `test_multiplicar_dois_negativos` |
    | **Entrada** | `a = -4`, `b = -6` |
    | **Resultado esperado** | `24` |
    | **Tipo** | Caso normal |

    Confirma a regra: negativo × negativo = positivo.

    ---

    ### Cenário 5 — Multiplicação com números decimais

    | Campo | Valor |
    |-------|-------|
    | **Nome** | `test_multiplicar_decimais` |
    | **Entrada** | `a = 2.5`, `b = 4.0` |
    | **Resultado esperado** | `10.0` |
    | **Tipo** | Caso normal |

    Verifica se a função funciona com `float`, não apenas com inteiros.

    ---

    ### Cenário 6 — Multiplicação por um (elemento neutro)

    | Campo | Valor |
    |-------|-------|
    | **Nome** | `test_multiplicar_por_um` |
    | **Entrada** | `a = 1`, `b = 99` |
    | **Resultado esperado** | `99` |
    | **Tipo** | Caso de borda |

    O número 1 é o elemento neutro da multiplicação: o resultado deve ser igual ao outro operando.

    ---

    ### Cenário 7 — Multiplicação de zero por zero

    | Campo | Valor |
    |-------|-------|
    | **Nome** | `test_multiplicar_zero_por_zero` |
    | **Entrada** | `a = 0`, `b = 0` |
    | **Resultado esperado** | `0` |
    | **Tipo** | Caso de borda |

    Combinação limite em que ambos os operandos são zero.

    ---

    ### Cenário 8 — Entrada inválida (tipo não numérico)

    | Campo | Valor |
    |-------|-------|
    | **Nome** | `test_multiplicar_entrada_invalida` |
    | **Entrada** | `a = "texto"`, `b = 5` |
    | **Resultado esperado** | `TypeError` (exceção lançada) |
    | **Tipo** | Caso de erro |

    A função atual não valida tipos. Em Python, `"texto" * 5` repete a string em vez de lançar erro. Para uma função de multiplicação matemática, o esperado costuma ser `TypeError` — o que exige validação na implementação ou ajuste do cenário de teste.

    ---

### Terminal após executar os testes 

PS C:\Users\Fax\Desktop\AtiviadeEngenhariaTeste\Engenharia-De-Software-Testes\teste-unitario-python> python  -m  unittest  test_calculadora.py
......
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
PS C:\Users\Fax\Desktop\AtiviadeEngenhariaTeste\Engenharia-De-Software-Testes\teste-unitario-python> python  -m  unittest  test_calculadora.py
..................
----------------------------------------------------------------------
Ran 18 tests in 0.002s

OK




## Uso de IA para geração de cenários de teste

  

### Função escolhida

  

`dividir(a, b)`

  

### Prompt utilizado

  

```Prompt-1


Atue como um professor de Teste de Software.

  

Tenho a seguinte função Python:

  
  

def dividir(a, b):

return a / b

  
  

Quero criar testes unitários usando unittest.

  

Liste cenários de teste para essa função, incluindo:

- divisão exata;

- divisão com resultado decimal;

- divisão de número negativo;

- divisão de zero por outro número;

- divisão por zero.

  

Para cada cenário, informe:

- nome do cenário;

- entrada;

- resultado esperado;

- tipo do cenário: caso normal, caso de borda ou caso de erro.

  

Não gere código ainda.








```
```Prompt-2
Transforme os cenários anteriores em testes unitários usando Python e unittest.

  

Considere que a função dividir(a, b) já foi importada.

  

Gere apenas os métodos de teste para serem colocados dentro da classe TestCalculadora.
```
```Prompt-3

Revise os testes unitários abaixo.

  

Verifique:

- se os métodos começam com test_;

- se os resultados esperados estão corretos;

- se há testes repetidos;

- se existem cenários importantes faltando;

- se há erro de importação;

- se os testes estão compatíveis com unittest.

  

Código:

      def test_dividir_divisao_exata(self):
        """Caso normal: divisão exata entre inteiros."""
        self.assertEqual(dividir(10, 2), 5)

    def test_dividir_resultado_decimal(self):
        """Caso normal: divisão com resultado decimal."""
        self.assertEqual(dividir(5, 2), 2.5)

    def test_dividir_numero_negativo(self):
        """Caso normal: dividendo negativo."""
        self.assertEqual(dividir(-10, 2), -5)

    def test_dividir_zero_por_numero(self):
        """Caso de borda: zero dividido por outro número."""
        self.assertEqual(dividir(0, 5), 0)

    def test_dividir_por_zero(self):
        """Caso de erro: divisão por zero deve gerar ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)

    def test_dividir_dois_negativos(self):
        """Caso normal: negativo dividido por negativo."""
        self.assertEqual(dividir(-12, -3), 4)

    def test_dividir_por_um(self):
        """Caso de borda: um é o elemento neutro da divisão."""
        self.assertEqual(dividir(7, 1), 7)

    def test_dividir_zero_por_zero(self):
        """Caso de erro: zero dividido por zero é indefinido."""
        with self.assertRaises(ZeroDivisionError):
            dividir(0, 0)    def test_dividir_divisao_exata(self):
        """Caso normal: divisão exata entre inteiros."""
        self.assertEqual(dividir(10, 2), 5)

    def test_dividir_resultado_decimal(self):
        """Caso normal: divisão com resultado decimal."""
        self.assertEqual(dividir(5, 2), 2.5)

    def test_dividir_numero_negativo(self):
        """Caso normal: dividendo negativo."""
        self.assertEqual(dividir(-10, 2), -5)

    def test_dividir_zero_por_numero(self):
        """Caso de borda: zero dividido por outro número."""
        self.assertEqual(dividir(0, 5), 0)

    def test_dividir_por_zero(self):
        """Caso de erro: divisão por zero deve gerar ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)

    def test_dividir_dois_negativos(self):
        """Caso normal: negativo dividido por negativo."""
        self.assertEqual(dividir(-12, -3), 4)

    def test_dividir_por_um(self):
        """Caso de borda: um é o elemento neutro da divisão."""
        self.assertEqual(dividir(7, 1), 7)

    def test_dividir_zero_por_zero(self):
        """Caso de erro: zero dividido por zero é indefinido."""
        with self.assertRaises(ZeroDivisionError):
            dividir(0, 0)


  

Explique os problemas encontrados em linguagem simples e sugira correções.

```



### Resposta do Prompt


```Prompt-1
### Função de referência


Em Python 3, a divisão com `/` retorna `float` quando o resultado não é inteiro (ex.: `5 / 2` → `2.5`). Divisão por zero lança `ZeroDivisionError`.

---

### Cenário 1 — Divisão exata

| Campo | Valor |
|-------|-------|
| **Nome** | `test_dividir_divisao_exata` |
| **Entrada** | `a = 10`, `b = 2` |
| **Resultado esperado** | `5.0` |
| **Tipo** | Caso normal |

Valida o fluxo principal: o dividendo é múltiplo do divisor e o resultado é um número inteiro (em Python 3, ainda assim retornado como `float` quando a operação é `/`).

---

### Cenário 2 — Divisão com resultado decimal

| Campo | Valor |
|-------|-------|
| **Nome** | `test_dividir_resultado_decimal` |
| **Entrada** | `a = 5`, `b = 2` |
| **Resultado esperado** | `2.5` |
| **Tipo** | Caso normal |

Garante que a função lida corretamente com quociente não inteiro.

---

### Cenário 3 — Divisão de número negativo

| Campo | Valor |
|-------|-------|
| **Nome** | `test_dividir_numero_negativo` |
| **Entrada** | `a = -10`, `b = 2` |
| **Resultado esperado** | `-5.0` |
| **Tipo** | Caso normal |

Confirma que o sinal do resultado está correto quando o dividendo é negativo.

---

### Cenário 4 — Divisão de zero por outro número

| Campo | Valor |
|-------|-------|
| **Nome** | `test_dividir_zero_por_numero` |
| **Entrada** | `a = 0`, `b = 5` |
| **Resultado esperado** | `0.0` |
| **Tipo** | Caso de borda |

Zero como dividendo é um valor limite: o resultado deve ser zero, desde que o divisor seja diferente de zero.

---

### Cenário 5 — Divisão por zero

| Campo | Valor |
|-------|-------|
| **Nome** | `test_dividir_por_zero` |
| **Entrada** | `a = 10`, `b = 0` |
| **Resultado esperado** | `ZeroDivisionError` (exceção lançada) |
| **Tipo** | Caso de erro |

Divisor zero é inválido em divisão aritmética. A função atual não trata esse caso — o Python propaga o erro automaticamente.

---

### Cenário 6 — Dois números negativos (complementar)

| Campo | Valor |
|-------|-------|
| **Nome** | `test_dividir_dois_negativos` |
| **Entrada** | `a = -12`, `b = -3` |
| **Resultado esperado** | `4.0` |
| **Tipo** | Caso normal |

Negativo ÷ negativo = positivo.

---

### Cenário 7 — Divisor igual a um (complementar)

| Campo | Valor |
|-------|-------|
| **Nome** | `test_dividir_por_um` |
| **Entrada** | `a = 7`, `b = 1` |
| **Resultado esperado** | `7.0` |
| **Tipo** | Caso de borda |

O número 1 é o elemento neutro da divisão: o resultado deve ser igual ao dividendo.

---

### Cenário 8 — Zero dividido por zero (complementar)

| Campo | Valor |
|-------|-------|
| **Nome** | `test_dividir_zero_por_zero` |
| **Entrada** | `a = 0`, `b = 0` |
| **Resultado esperado** | `ZeroDivisionError` (exceção lançada) |
| **Tipo** | Caso de erro |

Combinação limite em que dividendo e divisor são zero — matematicamente indefinida.

---
```
```Prompt-2

python
    def test_dividir_divisao_exata(self):
        """Caso normal: divisão exata entre inteiros."""
        self.assertEqual(dividir(10, 2), 5)

    def test_dividir_resultado_decimal(self):
        """Caso normal: divisão com resultado decimal."""
        self.assertEqual(dividir(5, 2), 2.5)

    def test_dividir_numero_negativo(self):
        """Caso normal: dividendo negativo."""
        self.assertEqual(dividir(-10, 2), -5)

    def test_dividir_zero_por_numero(self):
        """Caso de borda: zero dividido por outro número."""
        self.assertEqual(dividir(0, 5), 0)

    def test_dividir_por_zero(self):
        """Caso de erro: divisão por zero deve gerar ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)

    def test_dividir_dois_negativos(self):
        """Caso normal: negativo dividido por negativo."""
        self.assertEqual(dividir(-12, -3), 4)

    def test_dividir_por_um(self):
        """Caso de borda: um é o elemento neutro da divisão."""
        self.assertEqual(dividir(7, 1), 7)

    def test_dividir_zero_por_zero(self):
        """Caso de erro: zero dividido por zero é indefinido."""
        with self.assertRaises(ZeroDivisionError):
            dividir(0, 0)


### Mapeamento cenário → método

| Cenário | Método de teste | Assertiva utilizada |
|---------|-----------------|---------------------|
| Divisão exata | `test_dividir_divisao_exata` | `assertEqual` |
| Resultado decimal | `test_dividir_resultado_decimal` | `assertEqual` |
| Número negativo | `test_dividir_numero_negativo` | `assertEqual` |
| Zero ÷ número | `test_dividir_zero_por_numero` | `assertEqual` |
| Divisão por zero | `test_dividir_por_zero` | `assertRaises(ZeroDivisionError)` |
| Dois negativos | `test_dividir_dois_negativos` | `assertEqual` |
| Divisor igual a um | `test_dividir_por_um` | `assertEqual` |
| Zero ÷ zero | `test_dividir_zero_por_zero` | `assertRaises(ZeroDivisionError)` |

```

```Prompt-3
     ## Resumo geral

| Critério | Situação |
|----------|----------|
| Métodos começam com `test_` | ✅ Correto |
| Resultados esperados | ✅ Corretos |
| Testes repetidos | ❌ Há duplicações |
| Cenários importantes | ⚠️ Cobertura boa, com pequenas lacunas opcionais |
| Erro de importação | ✅ Sem erro (com imports existentes) |
| Compatibilidade com `unittest` | ✅ Compatível |

**Veredicto:** Os testes estão **logicamente corretos** e **funcionam** com `unittest`, mas o código apresentado tem **repetições** que devem ser removidas antes de considerar a suíte limpa e organizada.

---

## 1. Métodos começam com `test_`

**Status: ✅ Aprovado**

Todos os 8 métodos seguem a convenção exigida pelo `unittest`:

- `test_dividir_divisao_exata`
- `test_dividir_resultado_decimal`
- `test_dividir_numero_negativo`
- `test_dividir_zero_por_numero`
- `test_dividir_por_zero`
- `test_dividir_dois_negativos`
- `test_dividir_por_um`
- `test_dividir_zero_por_zero`

O framework só executa automaticamente métodos cujo nome começa com `test_` dentro de uma classe que herda de `unittest.TestCase`. Nesse ponto, está tudo certo.

---

## 2. Resultados esperados estão corretos

**Status: ✅ Aprovado**

| Método | Entrada | Esperado no teste | Resultado real de `dividir` | Correto? |
|--------|---------|-------------------|-----------------------------|----------|
| `test_dividir_divisao_exata` | `10, 2` | `5` | `5.0` | ✅ Sim (`5.0 == 5`) |
| `test_dividir_resultado_decimal` | `5, 2` | `2.5` | `2.5` | ✅ Sim |
| `test_dividir_numero_negativo` | `-10, 2` | `-5` | `-5.0` | ✅ Sim |
| `test_dividir_zero_por_numero` | `0, 5` | `0` | `0.0` | ✅ Sim |
| `test_dividir_por_zero` | `10, 0` | `ZeroDivisionError` | `ZeroDivisionError` | ✅ Sim |
| `test_dividir_dois_negativos` | `-12, -3` | `4` | `4.0` | ✅ Sim |
| `test_dividir_por_um` | `7, 1` | `7` | `7.0` | ✅ Sim |
| `test_dividir_zero_por_zero` | `0, 0` | `ZeroDivisionError` | `ZeroDivisionError` | ✅ Sim |

### Observação sobre floats

Em Python 3, `10 / 2` retorna `5.0` (float), não `5` (int). Mesmo assim, `self.assertEqual(dividir(10, 2), 5)` **passa**, porque Python considera `5.0` e `5` iguais.

Se quiser deixar o teste mais explícito para divisão, pode escrever:

```python
self.assertEqual(dividir(10, 2), 5.0)
```

Isso não é obrigatório — é apenas uma boa prática de clareza.

---

## 3. Testes repetidos

**Status: ❌ Problema encontrado**

Há **três tipos de repetição** no material analisado:

### Problema A — Bloco inteiro colado duas vezes

No código enviado para revisão, os **8 métodos aparecem duplicados** — o mesmo bloco foi colado duas vezes seguidas.

**Consequência:** Se isso for inserido no arquivo, você terá métodos com o **mesmo nome definidos duas vezes**. Em Python, a segunda definição **substitui** a primeira. O arquivo até pode rodar, mas fica confuso e difícil de manter.

### Problema B — `test_dividir_por_zero` definido duas vezes

Dentro do bloco duplicado, o método `test_dividir_por_zero` aparece **duas vezes** com implementações equivalentes:

```python
def test_dividir_por_zero(self):
    with self.assertRaises(ZeroDivisionError):
        dividir(10, 0)
```

**Correção:** Manter **apenas uma** versão desse método.

### Problema C — Conflito com `test_dividir` antigo (no arquivo do projeto)

No `test_calculadora.py` atual também existe o método antigo `test_dividir`:

```python
def test_dividir(self):
    self.assertEqual(dividir(10, 2), 5)      # repetido em test_dividir_divisao_exata
    self.assertEqual(dividir(9, 3), 3)       # cenário extra
    self.assertEqual(dividir(5, 2), 2.5)     # repetido em test_dividir_resultado_decimal
```

**Cenários já cobertos por outros métodos:**

| Cenário no `test_dividir` antigo | Já existe em |
|----------------------------------|--------------|
| `dividir(10, 2) == 5` | `test_dividir_divisao_exata` |
| `dividir(5, 2) == 2.5` | `test_dividir_resultado_decimal` |

**Correção sugerida:** Remover o método `test_dividir` antigo. Se quiser manter o caso `dividir(9, 3) == 3`, crie um método separado ou incorpore em `test_dividir_divisao_exata` com um segundo `assertEqual`.

### Problema D — Erro de formatação no código colado

No trecho enviado, há uma linha problemática:

```python
            dividir(0, 0)    def test_dividir_divisao_exata(self):
```

Faltou uma **quebra de linha** entre o fim de um método e o início do próximo.

**Consequência:** Isso gera **erro de sintaxe** (`SyntaxError`) e o arquivo não executa.

**Correção:** Garantir que cada `def test_...` comece em uma linha nova, com indentação de 4 espaços dentro da classe.

---

## 4. Cenários importantes faltando

**Status: ⚠️ Cobertura boa, com lacunas menores**

Os 5 cenários pedidos na atividade estão cobertos:

| Cenário solicitado | Método |
|--------------------|--------|
| Divisão exata | `test_dividir_divisao_exata` |
| Resultado decimal | `test_dividir_resultado_decimal` |
| Número negativo | `test_dividir_numero_negativo` |
| Zero ÷ número | `test_dividir_zero_por_numero` |
| Divisão por zero | `test_dividir_por_zero` |

Além disso, há cenários complementares úteis: dois negativos, divisor igual a 1 e zero ÷ zero.

### Cenários opcionais que ainda poderiam ser adicionados

| Cenário | Exemplo | Por quê? |
|---------|---------|----------|
| Divisor negativo | `dividir(10, -2) == -5` | Testa negativo no **divisor**, não só no dividendo |
| Entrada inválida | `dividir(None, 5)` → `TypeError` | Valida comportamento com tipo incorreto |
| Operandos decimais | `dividir(7.5, 2.5) == 3.0` | Garante divisão quando **ambos** são float |

Esses cenários **não são obrigatórios** para a atividade, mas aumentariam a robustez da suíte.

---

## 5. Erro de importação

**Status: ✅ Sem problema**

Os testes usam `dividir(...)` diretamente. Isso funciona porque o arquivo `test_calculadora.py` já possui:

```python
from calculadora import dividir, multiplicar, somar, subtrair, potencia, calcular_media
```

**Condições para não ter erro:**

1. O arquivo `calculadora.py` deve existir na mesma pasta (ou no `PYTHONPATH`).
2. Os métodos devem estar **dentro** da classe `TestCalculadora`, que herda de `unittest.TestCase`.
3. Não é necessário importar `dividir` novamente dentro de cada método.

Se os métodos forem colados **fora** da classe ou em outro arquivo sem o import, aí sim ocorreria `NameError: name 'dividir' is not defined`.

---

## 6. Compatibilidade com `unittest`

**Status: ✅ Compatível**

| Requisito do `unittest` | Atendido? |
|-------------------------|-----------|
| Classe herda de `unittest.TestCase` | ✅ (no arquivo do projeto) |
| Métodos nomeados com `test_` | ✅ |
| Uso de `self.assertEqual` | ✅ |
| Uso de `self.assertRaises` para exceções | ✅ |
| Bloco `with self.assertRaises(...)` | ✅ |

Os testes foram executados com:

```bash
python -m unittest test_calculadora.py -v
```

**Resultado:** 25 testes executados, todos passando (`OK`).
```

```
### Terminal após executar os testes 

PS C:\Users\Fax\Desktop\AtiviadeEngenhariaTeste\Engenharia-De-Software-Testes\teste-unitario-python> python  -m  unittest  test_calculadora.py
.........................
----------------------------------------------------------------------
Ran 25 tests in 0.002s

OK