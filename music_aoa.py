import numpy as np
from pyargus.directionEstimation import *
import matplotlib.pyplot as plt
import scipy.linalg as la

#TODO
def aoa():
    """
        Take Input sample signal array
        Return D angles of arrival

        Step by Step:
        transform antenna data input into correlation matrix calculation
        determine eigen decomposition
        Calculate MUSIC Spectrum Calc
        Return Estimation of largest peaks
    """
    ### Matrix correlation of input
    pass

    ### Eigen Decomp

    ### MUSIC Spectrum calc

    ### AOA Estimated Angles
#TODO
def fake_signal(M: int, d: float, N: int, K: int):
    """
        Generate random sinusoidal signal

        Parameters:
            M: Number of antenna elements in the array
            D: Inter-element spacing - Distance between antenna elements in centimeters
            N: number of incident signals
            K: number of data samples 
            
    """
    #K = 2**2 # Sample Size
    theta = 87 # Incident angle of the test signal

    # Steering Vector Matrix for input signal
    a = np.exp(np.arange(0,M)*1j*2*np.pi*d*np.cos(np.deg2rad(theta))) # Doesn't consider wavenumber incorrectly #TODO Fix

    # Generate multichannel test signal
    soi = np.random.normal(0,1,K) # Signal of interest
    soi_matrix = np.outer(soi,a).T

    # Generate multichannel uncorrelated noise
    noise = np.random.normal(0,np.sqrt(10**-10),(M,K))

    # Create received signal
    rec_signal = soi_matrix + noise
    return rec_signal

# Library Implementation: https://pypi.org/project/pyargus/

# Implement example with library as inspo for own implementation

if __name__ == "__main__":
    print(fake_signal(3, 1, 2, 10))
