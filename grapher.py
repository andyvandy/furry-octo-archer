from pylab import *
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




def main():
    if sys.argv[1] =='Pie':
        pie_plot(sys.argv[2])
    if sys.argv[1] =='ScatterColour':
        scatter_colour(sys.argv[2])
        
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

def scatter_colour(points):
    points = 1024
    X = np.random.normal(0,1,points)
    Y = np.random.normal(0,1,points)
    T = np.arctan2(Y,X)
    scatter(X,Y,  s=75, c=T, alpha=.5)
    xlim(-1.5,1.5), xticks([])
    ylim(-1.5,1.5), yticks([])
    show()
    

if __name__ == '__main__':
    commands= ['Pie', 'ScatterColour']
    command_help={
                "Pie":" use it like this -> grapher.py Pie int(slices)"
               ,"ScatterColour": " use it like this -> grapher.py ScatterColour int(points)"
    
                }
    if len(sys.argv)==1:
        print "Use help for information on how to use me! --> grapher.py help"
    if sys.argv[1]== 'help':
        if len(sys.argv)==2:
            print" use one of the following commands "
            print commands
        elif sys.argv[2] in commands:
            print command_help[command]
    main()