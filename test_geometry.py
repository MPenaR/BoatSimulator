import numpy as np 
from geometry_tools import compute_area

TOL = 1E-4 #tolerance for the tests
N = 400

# Test with a circle
def test_circle():
    R = 1  
    th = -np.linspace(0,2*np.pi,N)

    x =  R * np.cos(th)
    y =  R * np.sin(th)
    points = (x,y)
    assert np.isclose(compute_area(points), np.pi*R**2, TOL)

# Test with an ellipse
def test_ellipse():
    a = 3
    b = 4  
    th = np.linspace(0,2*np.pi,N)

    x = a * np.cos(th)
    y = b * np.sin(th)
    points = (x,y)
    assert np.isclose(compute_area(points), np.pi*a*b, TOL)

