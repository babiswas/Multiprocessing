from threading import Thread
from threading import Condition
from time import sleep
from queue import Queue
import random

queue=Queue()
condition=Condition()

class Producer(Thread):
     def run(self):
         while True:
           condition.acquire()
           queue.put(random.choice([i for i in range(10)]))
           print("Added task")
           condition.notify()
           condition.release()
           sleep(4)
          

class Consumer(Thread):
     def set_name(self,name,delay):
         self.name=name
         self.delay=delay
     def run(self):
        while True:
            condition.acquire()
            if queue.empty():
                 print(f"{self.name} waiting as queue is empty")
                 condition.wait()
            elem=queue.get()
            print(f"{self.name} is executing task")
            print("task "+str(elem))
            condition.release()
            sleep(self.delay)
            
            

if __name__=="__main__":
   p=Producer()
   c1=Consumer()
   c2=Consumer()
   c1.set_name("hello1",2)
   c2.set_name("hello2",2)
   p.start()
   c1.start()
   c2.start()
   p.join()
   c1.join()
   c2.join()
