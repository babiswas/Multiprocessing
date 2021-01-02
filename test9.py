from multiprocessing import Pool


def task(args):
    sum=0
    for i in args:
       sum=sum+i
    return sum

if __name__=="__main__":
   p=Pool(processes=5)
   data=p.map(task,[(1,2,3),(4,5,6),(7,8,9)])
   p.close()
   print(data)

   