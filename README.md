# Projeto Queue em Python

Implementação de uma fila FIFO utilizando Python.

## Arquivos do projeto

* `queue.py` -> contém a implementação da classe `Queue`
* `test_queue.py` -> contém os testes da fila

## Funcionalidades

A classe possui os seguintes métodos:

* `enqueue()` -> adiciona um item na fila
* `dequeue()` -> remove o primeiro item da fila
* `peek()` -> mostra o primeiro item sem remover
* `is_empty()` -> verifica se a fila está vazia
* `is_full()` -> verifica se a fila está cheia
* `size()` -> retorna a quantidade de elementos
* `clear()` -> limpa a fila

## Como executar

Execute o arquivo de testes com o comando:

```bash
python test_queue.py
```

## Observações

* A fila foi implementada utilizando lista (`list`)
* Não foi utilizado `collections.deque`
* O código possui tratamento de erros para fila vazia e fila cheia
