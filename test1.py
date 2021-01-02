from multiprocessing import Process
from time import sleep



def task(str1):
   print(f"{str1} recieved")
   sleep(2)
   print(f"{str1} processing")
   print(f"{str1} completed")


if __name__=="__main__":
   task_list=["task "+str(i) for i in range(10)]
   process_queue=[Process(target=task,args=(par,)) for par in task_list]
   for process in process_queue:
       process.start()
   for process in process_queue:
       process.join()
