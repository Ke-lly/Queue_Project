from queue import Queue

# Teste 1 - enqueue e size
fila = Queue()

fila.enqueue(10)
fila.enqueue(20)

assert fila.size() == 2
print("Teste 1 passou!")


# Teste 2 - dequeue
item = fila.dequeue()

assert item == 10
assert fila.size() == 1
print("Teste 2 passou!")


# Teste 3 - peek
assert fila.peek() == 20
assert fila.size() == 1
print("Teste 3 passou!")


# Teste 4 - fila vazia
fila.clear()

try:
    fila.dequeue()
except IndexError as e:
    print("Teste 4 passou!", e)


# Teste 5 - fila cheia
fila_limitada = Queue(max_size=2)

fila_limitada.enqueue(1)
fila_limitada.enqueue(2)

try:
    fila_limitada.enqueue(3)
except OverflowError as e:
    print("Teste 5 passou!", e)
