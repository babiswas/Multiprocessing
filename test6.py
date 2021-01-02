from concurrent.futures import ProcessPoolExecutor
from time import sleep
import concurrent.futures

def task(str1):
   print(f"Obtained task {str1}")
   sleep(2)
   print(f"Processing task {str1}")
   return f"Completed task {str1}"


if __name__=="__main__":
   with ProcessPoolExecutor() as executor:
      futures=[executor.submit(task,"task "+str(i)) for i in range(10)]
      done,not_done=concurrent.futures.wait(futures,return_when=concurrent.futures.ALL_COMPLETED)
      for fut in done:
         print(fut.result())
