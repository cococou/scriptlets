#!/usr/bin/env python3
import re,sys,os
sys.setrecursionlimit(1500)  

def is_file(path):
    files = os.listdir(path)
    dirs = []
    for i in files:
        full_path = os.path.join(path,i)
        if os.path.isdir(full_path):
            dirs.append(full_path)
            #is_file(full_path)
        else:
            print("     "+ i)
     
    for i in dirs:
        print("--- ",os.path.basename(i))
        is_file(i)

if __name__ == "__main__":
    try:
        path = sys.argv[1]
    except:
        path = os.getcwd()
    
    print("-- " + path)
    is_file(path)

    

