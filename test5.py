from threading import Thread
from queue import Queue
from time import sleep
import random


def task(*args):
   print(args)
   sum=0
   for i in args:
      sum+=i
   return sum

queue=Queue()


class Producer(Thread):
   def run(self):
      while True:
        queue.put((task,(random.choice([1,2,3]),random.choice([4,5,6]),random.choice([7,8,9]))))
        sleep(2)
        print("Task is queued")

class Consumer(Thread):
   def run(self):
      while True:
          if not queue.empty():
             function,args=queue.get()
             print(function(*args))
             sleep(4)
          else:
             break

if __name__=="__main__":
   p=Producer()
   c=Consumer()
   p.start()
   c.start()
   p.join()
   c.join()


         
      