from threading import Thread
from time import sleep

def task(str1):
   print(f"{str1} recieved")
   print(f"{str1} processed")
   sleep(2)
   print(f"{str1} completed")

if __name__=="__main__":
   task_list=["task "+str(i) for i in range(10)]
   thread_queue=[Thread(target=task,args=(par,)) for par in task_list]
   for thread in thread_queue:
        thread.start()
   for thread in thread_queue:
        thread.join()
