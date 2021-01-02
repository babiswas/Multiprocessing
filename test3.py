from threading import Thread
from time import sleep
from queue import Queue


def task(str1):
  print(f"{str1} recieved")
  sleep(2)
  print(f"{str1} processing")
  print(f"{str1} completed")



if __name__=="__main__":
   queue=Queue()
   task_list=["task "+str(i) for i in range(10)]
   task_queue=[]
   for i in range(10):
      queue.put(task)
   while not queue.empty():
      task_queue.append(Thread(target=queue.get(),args=(task_list.pop(),)))
   for task in task_queue:
      task.start()
   for task in task_queue:
      task.join()

      