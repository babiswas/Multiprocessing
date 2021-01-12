import argparse



if __name__=="__main__":
   parser=argparse.ArgumentParser()
   parser.add_argument('--test1',help="Add test1")
   parser.add_argument('--test2',help="Add test2")
   args=parser.parse_args()
   print(args.test1)
   print(args.test2)

   
   