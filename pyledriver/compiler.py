import re
class PyCompiler:
    def __init__(self, context):
        self._ctx = context
    def dict_from_model(self, col_names):
        d = {}
        for col_name in col_names:  
            key = col_name
            for char in col_name: 
                if not char.isalpha():
                    key = key.replace(char,'')        
            d[key] = col_name.replace('\'','').replace('  ','').strip()
        return d        
    
class ColumnCompiler(PyCompiler):
    def __init__(self, context): 
        PyCompiler.__init__(self, context)
    def Compile(self):    
        f = open(self._ctx.output_file_path) 
        txt = f.read().replace('\n','')
        regex = re.compile('\[(.*)\]', flags=re.IGNORECASE) 
        mtch = regex.search(txt)  
        model = mtch.group(1).split(',')
        d = self.dict_from_model(model) 
        s= '' 
        t = open(self._ctx.snippets)  
        snips = ('\n' + t.read()).split('\n%%')
        for snip in snips:
            s+='\n'
            for k in d:
                s+=snip.replace('$0',k).replace('$1',d[k])
  
        s+='\n\ndf=pd.DataFrame(d)' 
        return s
        
