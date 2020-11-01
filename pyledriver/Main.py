import os  
import matplotlib.pyplot as plt
from CleanerUppers import file_remover  
from CleanerUppers import dir_get_sizer 
from CleanerUppers import file_renamer 



path = r'C:\Users\Tim\Documents\WORK\_LEARN\MachineLearning\TTC - Big Data'
regexes = [  ".*\.m4v$"  ]
rfilter = "(" + ")|(".join(regexes) + ")"
file_renamer(path, rfilter)

#%%
curdir = os.getcwd()
regexes = [  ".*\.srt$", ".*\.vtt$"  ]
rfilter = "(" + ")|(".join(regexes) + ")"
path = 'C:\\Users\\Tim\\Documents\\WORK\\_LEARN\\MachineLearning\\'
file_remover(path, rfilter)

#%%
path = 'C:\\Users\\Tim\\Documents\\WORK\\_LEARN\\MachineLearning\\'
regexes = [  ".*\.mp4$", ".*\.wmv$", ".*\.mov$"  ]
rfilter = "(" + ")|(".join(regexes) + ")"
D = {} 
for k, v in dir_get_sizer( path , rfilter, 150 ):
    D[k]=v
    print(k)
    
plt.figure(figsize=(8,6))    
plt.bar(range(len(D)), list(D.values()), align='center')
plt.xticks(range(len(D)), list(D.keys()), rotation='vertical') 
plt.show()

  
