import json 
import os 
class ConfigProvider: 
    def __init__(self):
        self.output_file_path='c:\_som\_cache.txt'
        self.Provide()
    def Provide(self):  
        dir_path = os.path.dirname(os.path.realpath(__file__))
        config_path = dir_path +'\\'+'config.json'
        #print(config_path)
        with open(config_path) as f:
          jsondata = json.load(f)
          dir_path = '\\'.join(dir_path.split('\\')[:-1])
          self.editor_path = jsondata['editor_path']
          self.output_file_path = jsondata['output_file_path'] 
          self.snippets = dir_path +'\\'+ jsondata['snippets'] 
          
       


    
    
    