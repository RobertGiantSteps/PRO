from __future__ import annotations


class IntegerStack:
    """
    Pila de enteros:
    ╔═════╗
    ║ TOP ║
    ╠═════╣
    ║   4 ║
    ║   3 ║
    ║   5 ║
    ║   7 ║
    ╚═════╝
    """

    def __init__(self, *, max_size: int = 10):
        """Utilizar atributo items para guardar los elementos"""
        self.max_size = max_size
        self.items = []

    def push(self, item: int) -> bool:
        """Añade item a la pila.
        Si la pila está llena retornar False, en otro caso retornar True"""
        size = len(self.items)
        if size < self.max_size:
            self.items.insert(0, item)
            return True
        else:
            return False

    def pop(self) -> int:
        """Extraer el elemento que está en el TOP de la (lista)"""
        top = self.items.pop(0)
        return top

    def top(self) -> int:
        """Devolver el elemento que está en el TOP de la pila (sin extracción)"""
        top = self.items[0]
        return top

    def is_empty(self) -> bool:
        """Indica si la pila está vacía"""
        return len(self.items) == 0

    def is_full(self) -> bool:
        """Indica si la pila está llena -> max_size"""
        return len(self.items) == self.max_size

    def expand(self, factor: int = 2) -> None:
        """Expande el tamaño máximo de la pila en el factor indicado"""
        self.max_size *= factor

    def dump_to_file(self, path: str) -> None:
        """Vuelca la pila a un fichero.
        - Cada item en una línea.
        - El primer elemento del fichero corresponde con el TOP de la pila."""
        with open(path, "w") as f:
            for item in self.items:
                f.write(str(item) + "\n")
        with open(path, "r") as f:
            contents = f.read()
        with open(path, "w") as f:
            f.write(contents[:-1])


    
    @classmethod
    def load_from_file(cls, path: str) -> 'IntegerStack':
        """Crea una pila desde un fichero.
        - Un item por línea.
        - El primer elemento del fichero corresponde con el TOP de la pila.
        - Si la pila se llena al ir añadiendo elementos habrá que expandir con los valores por defecto"""
        stack = cls()
        with open(path, "r") as f:
            top = int(f.readline())
            stack.items.append(top)
            for line in f:
                item = int(line.strip())
                if len(stack.items) < stack.max_size:
                    stack.items.append(item)
                else:
                    stack.expand()
                    stack.items.append(item)
        while len(stack.items) < stack.max_size:
            stack.expand()
        return stack.items
            
            
                
 

    def __getitem__(self, index: int) -> int:
        """Devuelve el elemento de la pila en el índice indicado"""
        return self.items[index]

    def __setitem__(self, index: int, item: int) -> None:
        """Establece el valor de un elemento de la pila mediante el índice indicado"""
        self.items[index] = item

    def __len__(self):
        """Número de elementos que contiene la pila"""
        elements = len(self.items)
        return elements

    def __str__(self):
        """Cada elemento en una línea distinta empezando por el TOP de la pila"""
        msg = "\n".join(str(item) for item in self.items)
        return msg

    def __add__(self, other: IntegerStack) -> IntegerStack:
        """Suma dos pilas.
        La segunda pila se coloca encima de la primera.
        La pila resultante tiene un tamaño máximo igual a la suma
        de los tamaños máximos de las dos pilas.
        """
        max_size = self.max_size + other.max_size
        result_stack = IntegerStack(max_size=max_size)

        # Copiar los elementos de la primera pila a la pila resultante
        for item in reversed(self.items):
            if not result_stack.is_full():
                result_stack.push(item)
            else:
                break

        # Copiar los elementos de la segunda pila a la pila resultante
        for item in reversed(other.items):
            if not result_stack.is_full():
                result_stack.push(item)
            else:
                break

        return result_stack




    def __iter__(self) -> IntegerStackIterator:
        return IntegerStackIterator(self)


class IntegerStackIterator:
    def __init__(self, stack: IntegerStack):
        self.stack = stack
        self.current_index = 0

    def __next__(self) -> int:
        if self.current_index >= len(self.stack):
            raise StopIteration
        value = self.stack[self.current_index]
        self.current_index += 1
        return value
