import glob
import os
import sys
import pathlib
import subprocess
import cclib
import pandas as pd
from os.path import exists

orig_dir='/home2/gridsan/jmaalouf/vHTP/Code/ylide/Library/Calcs'

df=pd.read_csv('Ylides_YlideRads.csv')
y=df['Ylides'].to_list()
yr=df['Ylides Rad'].to_list()
yh=df['Ylides H'].to_list()

n=len(y)

for i in range(2):
    suffix_list=['','_rad','_h']
    
    for suff in suffix_list:
        
        
        
        path=pathlib.Path(os.path.join(orig_dir, str(i).zfill(7) , f'ylide{suff}', f'{str(i).zfill(7)}_ylide{suff}.sh'))
        par_path=path.parent.absolute()
        filename=os.path.basename(os.path.normpath(path))
        
        #GET LOG FILE NAME
        split_file=filename.split('.')
        log_file=f'{split_file[0]}.log'
        
        os.chdir(par_path)
        subprocess.run(f'sbatch {filename}',shell=True)
        os.chdir(orig_dir)
        