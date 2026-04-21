import numpy as np
from astropy.table import Table


def main():
    x = np.linspace(0,2*np.pi,1000)
    sinx = np.sin(x)
    data = Table([x,sinx],names=['x','sinx'])
    print(data)
    
if __name__ == "__main__":
    main()