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
    ax.set_xlim(0,10)    #(0, 2*np.pi)-previous was 2 x pi or68.28
    ax.set_ylim(0, 400)  #(-1, 1) previously for sin wave
    return ln,

def update(frame):
    po = round(np.random.normal(2,1))
    xdata.append(po)        #xdata.append(round(np.random.normal(2,1)))            #xdata.append(frame)
    
    count = 0
    for i in xdata:
        if i == po:
            count = count +1
            print (count)
    
    ydata.append(count)
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 10, 200),
                    init_func=init, blit=True)
					
from matplotlib.animation import FFMpegWriter,
writer = FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800),
ani.save("Normal_distribution.mp4", writer=writer),
					
plt.show()

