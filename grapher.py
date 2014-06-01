from pylab import *
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




def main():
    if sys.argv[1] =='pie':
        pie_plot(sys.argv[2])
        
def pie_plot(slices):        
    slices = 20
    Z = np.ones(slices)
    Z[-1] *=2
    axes([0.025,0.025,0.95,0.95])
    pie(Z, explode= Z*0.05,colors = ['%f' % (i/float(slices)) for i in range(slices)]) 
    gca().set_aspect('equal')
    xticks([])
    yticks([])
    savefig('figures/pie_ex.png',dpi=48)
    show()


if __name__ == '__main__':
    if len(sys.argv)==1:
        print " you need to add parameters: grapher.py pie slices "
    main()