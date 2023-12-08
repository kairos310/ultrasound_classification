import matplotlib
import matplotlib.pyplot as plt
import os
import numpy as np
import tensorflow as tf

data = []
names = []
for filename in os.listdir(os.getcwd() + "\data"):
    print("reading", filename)
    measure = []
    names.append(filename)
    with open(os.path.join(os.getcwd() + "\data", filename), 'r') as f: # open in readonly mode
        
        rows = f.read().splitlines()
        for i,r in enumerate(rows):
            if(i == 100):
                break
            col = r.split("\t")
            measure.append(col)
        data.append(measure)
for i, d in enumerate(data):
    print(len(d))
    print(names[i])
data = np.array(data, dtype=float)
print(data)
plt.plot(data[0])