from queue import PriorityQueue


def task1():
  print("Task1 executed")

def task2():
  print("Task2 executed")

def task3():
  print("Task3 executed")

def task4():
  print("Task4 executed")

def task5():
  print("Task5 executed")

def task6():
  print("Task6 executed")



queue=PriorityQueue()
queue.put((1,task1))
queue.put((3,task3))
queue.put((2,task4))
queue.put((6,task6))
queue.put((4,task4))
queue.put((5,task5))


if __name__=="__main__":
   while not queue.empty():
       queue.get()[1]()


    

