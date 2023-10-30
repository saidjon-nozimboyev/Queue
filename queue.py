#STACK - LIFO
#QUEUE - FIFO 
from time import sleep
class Queue:

    def __init__(self) -> None:
        self.data = []
        self.__size = 0 


    def enqueue(self, v:any) -> None:
        self.data.append(v)
        self.__size += 1 

    def empty(self) -> bool:
        return self.__size == 0 
    
    def dequeue(self) -> any:
        if not self.empty():
            self.__size -= 1 
            return self.data.pop(0)
        else:
            raise Exception("Queue is empty")
    
    def front(self) -> any:
        if not self.empty():
            return self.data[0]
        else:
            raise Exception("Queue is empty")
        
    def clear(self):
        self.data.clear()

    @property
    def Size(self):
        return self.__size 
    
class Clients:

    def __init__(self, name = "", time = 1) -> None:
        self.name = name 
        self.time = time 

if __name__ == "__main__":
    clients = [Clients("Said", 1), 
               Clients("Rustamjon", 4), 
               Clients("Ali", 2), 
               Clients("Vali", 2)]
    q_market = Queue()
    for client in clients:
        q_market.enqueue(client)
    while not q_market.empty():
        qu:Clients = q_market.dequeue()
        print(f"Service is been provided for {qu.name}...")
        sleep(qu.time)
