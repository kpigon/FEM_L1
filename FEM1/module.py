import numpy as np

def rownanie(x1):
    x=[]
    for i in range (0,np.size(x1)):
        if (x1[i] < 0.0):
            x.append(np.sin(x1[i]))
        else:
            x.append(np.sqrt(x1[i]))
    return x