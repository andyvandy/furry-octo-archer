"""This file uses the main GUI generated and implements the canvas and various functions"""
import numpy as np
import wx
import GUIbase


import matplotlib
matplotlib.use('WXAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import \
        FigureCanvasWxAgg as FigCanvas, \
        NavigationToolbar2WxAgg as NavigationToolbar
from pylab import * 


#place all features in this list
commands= ['Pie', 'ScatterColour']

 
class MyFrameSub(GUIbase.MyFrame1):

    def __init__(self, parent):
        GUIbase.MyFrame1.__init__(self, parent)
        self.InitUI()
        
    def InitUI(self):
        #filling out GUI things
        for command in commands: 
            self.m_functionscombo.Append(command)
        
        #binding events
        self.m_button2.Bind(wx.EVT_BUTTON, self.generate_fun)
        self.Bind(wx.EVT_MENU, self.OnExit, self.m_file_quit)
        self.m_button3.Bind(wx.EVT_BUTTON, self.end_fun)
        self.m_functionscombo.Bind(wx.EVT_COMBOBOX,self.options)
    def CreateCanvas(self):
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigCanvas(self.m_canvas, wx.ID_ANY, self.figure)
        self.Fit()
    def HideyoWife (self):
        self.m_checkBox4.Hide()
        self.m_checkBox5.Hide()
        self.m_checkBox6.Hide()
        self.m_checkBox7.Hide()
        self.m_staticText_field1.Hide()
        self.m_textCtrl_field1.Hide()
        self.m_staticText_field2.Hide()
        self.m_textCtrl_field2.Hide()
        self.m_staticText_field3.Hide()
        self.m_textCtrl_field3.Hide()
    
    def options(self, e):
        self.HideyoWife()
        selection= self.m_functionscombo.GetValue()
        if selection =="Pie":pie_plot_options(self)
        elif selection =="ScatterColour": scatter_colour_options(self)
        #acts as aswitch board and sets the options for each feature
    
    def generate_fun(self, e):
        selection =commands[self.m_functionscombo.GetCurrentSelection()]
        if selection =="Pie": pie_plot( int(self.m_textCtrl_field1.GetValue()),self)
        elif selection =="ScatterColour": scatter_colour(int(self.m_textCtrl_field1.GetValue()),self)
        self.canvas = FigCanvas(self.m_canvas, wx.ID_ANY, self.figure)
        #acts as the switchboard and gets stuff onto the plot
    
    def end_fun(self, e):
        self.figure.clf()
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigCanvas(self.m_canvas, wx.ID_ANY, self.figure)
        #clears the plot
    
    def OnExit(self,e):
        print"pooo"
        plt.close('all') # if you don't have this the program won't terminate
        self.Close(True)
        
#Functions are below!________________________________________________________________    

#------- Pies   
def pie_plot(slices,self):
    Z = np.ones(slices)
    Z[-1] *=2
    #self.figure.add_axes([0.025,0.025,0.95,0.95])
    self.axes.pie(Z, explode= Z*0.05,colors = ['%f' % (i/float(slices)) for i in range(slices)]) 
    gca().set_aspect('equal')
    xticks([])
    yticks([])

def pie_plot_options(self):
    
    self.m_staticText_field1.Show()
    
    self.m_textCtrl_field1.Show()
    self.m_staticText_field1.SetLabel("Slices")
#------ Pies
    
#---Scatter colour    
def scatter_colour(points,self):
    X = np.random.normal(0,1,points)
    Y = np.random.normal(0,1,points)
    T = np.arctan2(Y,X)
    self.axes.scatter(X,Y,  s=75, c=T, alpha=.5)
    xlim(-1.5,1.5), xticks([])
    ylim(-1.5,1.5), yticks([])
def scatter_colour_options(self):
    
    self.m_staticText_field1.Show()
    self.m_textCtrl_field1.Show() 
    self.m_staticText_field1.SetLabel("Points")
#---Scatter colour     
        
#Functions are above! _________________________________________    
if __name__=='__main__':        
    print commands
    app = wx.App()
    window = MyFrameSub(None)
    thing= window.CreateCanvas()
    window.Show(True)
    app.MainLoop()