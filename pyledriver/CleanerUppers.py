import os
import re
from os import walk
from os.path import join 
dirs = [] 
fnames = [] 
def file_remover(path, regex):
    for root, dirnames, filenames in walk(path):
        for fname in filenames:
            fullname = join(root,fname)
            if re.match(regex, fname):  
                fnames.append(fullname) 
                print(fullname)  
    command = input("delete? y/n")
    if command == 'y':
        for f in fnames:
            try:
                 os.remove(f) 
            except:
                 pass           
            
def file_renamer(path, regex):
    with open(path + '\\titles.txt', 'r') as reader: 
         titles = reader.read().split('\n')
    fcnt = 0          
    for root, dirnames, filenames in walk(path):
        for fname in filenames:
            fullname = join(root,fname)
            if re.match(regex, fname):  
                #print(fname + '  ' + titles[fcnt]) 
                #os.rename(fullname, join(root,titles[fcnt]) + '.m4v')
                fcnt=fcnt+1
                
                
                
def dir_get_sizer(path, regex, thresh=100):
    dict = {} 
    for root, dirnames, filenames in walk(path):
        total_size = 0 
        for fname in filenames: 
            fullname = join(root,fname)   
            if re.match(regex, fullname): 
                try:
                    total_size += os.path.getsize(fullname)/1000000     
                except:
                    total_size += 0
        if total_size > thresh:  
            key = ''.join(fullname.replace(path, '').split('\\')[1])
            if not key in dict.keys():
                dict[key] =  round(total_size) 
                yield key, dict[key]
                
        
    #return dict  
    
     
                