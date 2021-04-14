import numpy as np
import pandas as pd
f=[]
for d in range(1,27):
    f.append(d)   
i=list(np.arange(97,123,1))   
b=[]
for c in i:
    a=chr(c)
    b.append(a)
s=pd.Series(f,index=b)
print(s)