import pandas as pd
import numpy as np
import xarray as xr
from alias_period import tidal_aliasing

constituent = ["2N2","EP2","J1","L2","M3","M4","MF","MI2","MKS","MM","MN4","MS4","MSF","MSQ"
            ,"MTM","N4","NI2","R2","S1","SA","SSA","T2",'M2','S2','N2','K2','K1','O1','P1','Q1']

catfile = "../data/catHW95.dat"

tt = tidal_aliasing(constituent,catfile,'jason-1',output='dataframe')
