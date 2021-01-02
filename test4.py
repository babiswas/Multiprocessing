from threading import Thread
from time import sleep
import random
from queue import Queue



queue=Queue()

def task(str1):
  print(f"{str1} obtained")
  sleep(2)
  print(f"Processing {str1}")
  print(f"Completed {str1}")


class Producer(Thread):
   def run(self):
      while True:
         queue.put((task,"task "+str(random.choice([1,2,3,4]))))
         print("Queued a task")
         sleep(2)

class Consumer(Thread):
   def run(self):
      while True:
         if not queue.empty():
            function,task=queue.get()
            function(task)
            queue.task_done()
            sleep(2)
         else:
            break
          
if __name__=="__main__":
   p=Producer()
   c=Consumer()
   p.start()
   c.start()
   p.join()
   c.join()

   