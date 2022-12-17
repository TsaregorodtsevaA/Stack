
class Stack():

    def __init__(self):
        self.stack = []


    def is_empty(self): # проверка стека на пустоту. Метод возвращает True или False.
        return not bool(self.stack)


    def push(self, item): #добавляет новый элемент на вершину стека. Метод ничего не возвращает.
        self.stack.append(item)


    def pop(self): #удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
        last = self.stack.pop()
        return last


    def peek(self): #возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
        return self.stack[-1]


    def size(self): #возвращает количество элементов в стеке.
        return len(self.stack)


smth=Stack()


def find_balance(some_str):
    for el in some_str:
        if el in '([{':
            smth.push(el)
        elif el in ')]}':
            if smth.is_empty()==False:
                the_last = smth.pop()
                if el==')' and the_last=='(':
                    continue
                elif el==']' and the_last=='[':
                    continue
                elif el=='}' and the_last=='{':
                    continue
                return 'Несбалансировано' #потому что скобки не те'
            else:
                return 'Несбалансировано' #потому что нет открывающих скобок'
    if smth.is_empty()==True:
        return 'Сбалансировано'
    else:
        return 'Несбалансировано' #потому что нет закрывающих скобок.'
