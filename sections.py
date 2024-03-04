'''module for defining and plotting sections of the boat's hull'''
import numpy as np 

def create_parts( board, port_data = False, N=10):
    '''Creates a section given the shape of a board'''
    x, y = board

    if port_data:
        x = -x
     
    starboard = x, y
    port = -x, y
    deck = np.linspace(x[-1], -x[-1], N), np.full(N,y[-1])

    return port, starboard, deck