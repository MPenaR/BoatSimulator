'''Module for ploting tools which are not necessarily interesting for boat entusiats'''

import matplotlib.pyplot as plt 
def plot_sea(h, ax=None, xmin=-2, xmax=2):
    '''plots the sea. Right now as an horizontal blue line.'''
    if ax is None:
        fig, ax = plt.subplots()

    ax.hlines(y=h,xmin=xmin,xmax=xmax,colors='b')



def plot_hull(points, under_region=None, ax = None):
    '''Plots the hull and the underwater region.
    '''
    if ax is None:
        fig, ax = plt.subplots()



    x, y = points[:,0], points[:,1]
    ax.plot(x,y,'.-',markerfacecolor='b', markeredgecolor='k')
    if under_region is not None:
        x_under, y_under = under_region[:,0], under_region[:,1]
        ax.fill(x_under,y_under, facecolor='gray', hatch='////')
