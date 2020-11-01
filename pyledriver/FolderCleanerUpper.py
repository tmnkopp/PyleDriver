import os
import re
from os import walk
from os.path import join 
dirs = [] 
curdir = os.getcwd()
regexes = [
    ".*\.srt$",
    ".*\.vtt$",
    "qu*x"]
#file_remover(curdir, remove_with)
combine_rex = "(" + ")|(".join(regexes) + ")"


def file_remover(path, rex):
    for root, dirnames, filenames in walk(path):
        for fname in filenames:
            fullname = join(root,fname)
            if re.match(rex, fname):  
                print(fullname)
                #os.remove(fullname) 

def dir_get_sizer(path):
    for root, dirnames, filenames in walk('C:\\Users\\Tim\\Documents\\WORK\\_LEARN\Angular\\'):
        total_size = 0
        for dr in dirnames:
            dirs.append(dr) 
        for fname in filenames:
            fullname = join(root,fname)
            #if re.match(".*.srt$", fname):  
                #os.remove(fullname) 
            if re.match(".*mp4$", fullname): 
                    total_size += os.path.getsize(fullname)    
                
    print(total_size/1000)    
    
    

    
                