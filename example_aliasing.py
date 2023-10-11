# load interested modules
import pandas as pd
import numpy as np
from alias_period import tidal_aliasing

# provide the constituents that you are interested in.

constituent = ["2N2","EP2","J1","L2","M3","M4","MF","MI2","MKS","MM","MN4","MS4","MSF","MSQ"
            ,"MTM","N4","NI2","R2","S1","SA","SSA","T2",'M2','S2','N2','K2','K1','O1','P1','Q1']

# provide the catalogue of harmonic constants used, this case is taken from https://doi.org/10.1029/95GL03324
catfile = "data/catHW95.dat"

# aliasing periods derived for respective altimetry missions 
# output is a list of the constituents and their respective aliasing period.

alias_j1 = tidal_aliasing(constituent,catfile,'jason-1',output='array')
alias_en = tidal_aliasing(constituent,catfile,'envisat',output='array')
alias_s3 = tidal_aliasing(constituent,catfile,'s3',output='array')
alias_cr = tidal_aliasing(constituent,catfile,'cry',output='array')
