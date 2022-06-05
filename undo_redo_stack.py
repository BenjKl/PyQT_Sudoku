from collections import deque


class UndoRedo:
    def __init__(self):
        self._stack = deque()
        self._index = -1

    def append(self, num):
        self.pop()
        self._stack.append(num)
        self._index += 1

    def pop(self):
        l = len(self._stack)
        for i in reversed(range(self._index + 1, l)):
            self._stack.pop()

    def undo(self):
        if self._index > 0:
            self._index -= 1

    def undoText(self):
        i = self._index
        if i > 0:
            return self._stack[i - 1]
        else:
            return self._stack[0]

    def redo(self):
        indx = len(self._stack)
        if self._index < (indx - 1):
            self._index += 1

    def redoText(self):
        indx = len(self._stack)
        i = self._index
        if i < (indx - 1):
            return self._stack[i + 1]
        else:
            return self._stack[indx - 1]

    def undoAvailable(self):
        if self._index > 0:
            return True
        else:
            return False

    def redoAvailable(self):
        l = len(self._stack)
        if self._index < l - 1:
            return True
        else:
            return False

    def out(self):
        return self._stack
        
    def current(self):
        return self._stack[self._index]
        
if __name__ == "__main__":
    stack = UndoRedo()        
    
    stack.append(1)
    stack.append(2)
    stack.append(3)    
    
    print("stack is:")
    print(stack.out())
    print(stack.current())

    print()    

    stack.undo()
    print("after undo:")
    print(stack.out())
    print(stack.current())    

    
    print()        
    
    stack.undo()
    print("after undo:")
    print(stack.out())
    print(stack.current())    
    
    print()        
    
    if stack.redoAvailable():
        stack.redo()
        print("after redo:")
        print(stack.out())
        print(stack.current())    
    else:
        print("redo not possible")

        
    
    print()
    
    stack.append(4)
    print("after append")
    print(stack.out())
    print(stack.current())        
    
    print()        
    
    if stack.undoAvailable():
        stack.undo()
        print("after undo:")
        print(stack.out())
        print(stack.current())    
    else:
        print("Undo not possible")
    
    if stack.undoAvailable():
        stack.undo()
        print("after undo:")
        print(stack.out())
        print(stack.current())    
    else:
        print("Undo not possible")

    if stack.undoAvailable():
        stack.undo()
        print("after undo:")
        print(stack.out())
        print(stack.current())    
    else:
        print("Undo not possible")

        
 
