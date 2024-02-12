class LimitedQueue:

    def __init__(self, max_n):
        self.max_n = max_n
        self.queue = [None] * self.max_n
        self.head = 0  # Голова указывает на индекс 0
        self.tail = 0  # Хвост указывает на индекс 0
        self.size = 0  # При создании очередь пуста, её длина - 0

    def is_empty(self):
        return self.size == 0
  
    def push(self, value):
        if self.queue[self.tail] is not None:
            self.head = (self.head + 1) % self.max_n
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.max_n
        if self.size < self.max_n:
            self.size += 1
    
    def pop(self):
        # Если очередь пуста...
        if self.is_empty():
            # ...возвращаем None.
            return None
        # Получаем значение элемента с индексом, на который указывает head:
        value = self.queue[self.head]
        # Вставляем на место этого значения None:
        self.queue[self.head] = None
        # Значение head должно увеличиться на единицу или
        # "спрыгнуть на ноль", если его значение будет равно max_n.
        # Применим тот же трюк, что и с tail:
        self.head = (self.head + 1) % self.max_n
        # Уменьшаем счётчик элементов в очереди.
        self.size -= 1
        # Возвращаем значение, на которое указывала голова:
        return value

# Начинаем проверку! Создаём очередь с ограничением 8 элементов:
q = LimitedQueue(8) 
q.push(1)  # Добавляем один элемент.
print('Очередь с одним элементом:', q.queue)
print('Длина очереди с одним элементом:', q.size)
# Добавляем ещё три элемента:
q.push(-1)
q.push(0)
q.push(11)
print('Очередь с четырьмя элементами:', q.queue)
print('Длина очереди с четырьмя элементами:',q.size)