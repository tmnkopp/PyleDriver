import subprocess 
from pyomatic.compiler import ColumnCompiler 
from pyomatic.context import ConfigProvider

class CodeGen: 
    def __init__(self):
        self._ctx = ConfigProvider() 
        self.df = '' 
        self.Generate()
    def Generate(self):  
        with open(self._ctx.output_file_path, 'w') as file: 
            file.write("['paste','columns','here']") 
        subprocess.call([self._ctx.editor_path, self._ctx.output_file_path]) 
        txt = ColumnCompiler(self._ctx).Compile() 
        if self._ctx.editor_path.strip() != '': 
            with open(self._ctx.output_file_path, 'w') as file: 
                file.write(txt) 
            subprocess.call([self._ctx.editor_path, self._ctx.output_file_path])  
       