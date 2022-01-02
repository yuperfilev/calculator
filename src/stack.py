from typing import Union

class Node:

    def __init__(self, value: Union[str, float]) -> None:
        self.value = value
        self.next = None

class Stack:
    
    def __init__(self) -> None:
        self.__head = None

    def push(self, value: Union[str, float]) -> None:
        node = Node(value)
        if self.__head is None:
            self.__head = node
        else:
            node.next = self.__head
            self.__head = node
    
    def pop(self) -> Union[str, float, None]:
        if self.__head is not None:
            value = self.__head.value
            self.__head = self.__head.next
            return value
        else:
            return
    
    def head(self) -> Union[str, float, None]:
        if self.__head is not None:
            return self.__head.value
        else:
            return
