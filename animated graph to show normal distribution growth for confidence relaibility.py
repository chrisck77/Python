#routine to display to demonstrate how to build a normal distribution from multiple samples of 10 taken from a larger population
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
%matplotlib notebook

marbles_df = pd.read_csv('C:\Data_Science\Reliabilty training graph animated\marbles.csv')
marbles_df.head(5)

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')

def init():
    ax.set_xlim(0,10)    #X axis
    ax.set_ylim(0, 400) 
    return ln,

def update(frame): #updates each frame of the animation
    po = round(np.random.normal(2,1)) #random number from a normal sample distribution with stdev 1, mean 2
    xdata.append(po)           
    count = 0
    for i in xdata:
        if i == po:
            count = count +1
            print (count)    
    ydata.append(count)
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames = 200, init_func=init, blit=True) #animation
			
#now save the animation to a mp4 file.FFmpeg needs to be installed via conda/pip install or windows download
from matplotlib.animation import FFMpegWriter, 	
writer = FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800),
ani.save("Normal_distribution.mp4", writer=writer),
					
plt.show()
