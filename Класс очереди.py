class Queue:

    def __init__(self):
        # Как и для стека, используем для хранения элементов очереди список.
        self.__items = []

    def push(self, item):
        """Добавить элемент в очередь."""
        # В отличие от стека, здесь добавляем элемент не в конец списка,
        # а в начало - на место элемента с индексом 0.
        self.__items.insert(0, item)

    def pop(self):
        """Вернуть элемент из очереди."""
        return self.__items.pop()

    def peek(self):
        """Вернуть последний элемент, но не удалять его из очереди."""
        return self.__items[-1]

    def size(self):
        """Вернуть размер очереди."""
        return len(self.__items) 