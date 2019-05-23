import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib notebook

# define Weibull constants
beta = 1.563528
eta = 72.713169

def weib(x,eta,beta):
    return (beta / eta) * ((x / eta)**(beta - 1)) * np.exp(-(x / eta)**beta)

x_fill = np.arange(0, 50, 1) # seperate range to highlight part of graph
y_fill = weib(x_fill,eta,beta)

#calculate the weibull values
xw = np.arange(1,200,1)
yw = weib(xw,eta,beta)


# plot settings
fig, ax = plt.subplots(figsize=(9,6))
plt.style.use('fivethirtyeight')
ax.set_xlim(0,150)
ax.set_ylim(0,0.012)
ax.set_title('Weibull Curve_PDF')
ax.set_ylabel('PDF')

# draw the plot
ax.plot(xw,yw)
ax.fill_between(x_fill,y_fill,0, alpha=0.3, color='b')

# save the plot
plt.savefig('weibull_PDF_curve.png', dpi=72, bbox_inches='tight')

plt.show()


##CDF PLOT 
# define Weibull constants
beta = 1.563528
eta = 72.713169



def weib2(x,eta,beta):
    return 1 -  np.exp(-(x / eta)**beta)

#calculate the weibull values
xw = np.arange(1,200,1)
yw = weib2(xw,eta,beta)

#calculate variables for drawing a line where x = 50 meets the curve
y_at_50 = 1 -  np.exp(-(50 / eta)**beta)
y_less_50 = np.ones(50)*y_at_50
x_less_50 = np.arange(0,50,1)

# plot settings
fig, ax = plt.subplots(figsize=(9,6))
ax.set_xlim(0,150)
ax.set_ylim(0,1)
ax.set_ylabel('CDF')

# draw the plot
ax.plot(xw,yw)
ax.plot(x_less_50,y_less_50, color='r') #draw a line at where x = 50 meets the curve

# save the plot
plt.savefig('weibull_CDF_curve.png', dpi=72, bbox_inches='tight')

plt.show()
