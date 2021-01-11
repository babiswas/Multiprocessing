from multiprocessing import Pipe,Process
from time import sleep

def child_proc(conn):
   conn.send("hello")
   sleep(3)
   print(conn.recv())
   conn.close()

if __name__=="__main__":
   parent_conn,child_conn=Pipe()
   p=Process(target=child_proc,args=(child_conn,))
   p.start()
   print(parent_conn.recv())
   parent_conn.send("hi")
   p.join()
