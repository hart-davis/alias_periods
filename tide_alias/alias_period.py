def tidal_aliasing(constituent, catfile, altimetry_mission, output=None, cat_header=0,
                  skip_rows_in_catfile=1, P = 0):

    """
    constituent: this is the constituents for which the alias period should be estimated.
    catfile: this is the catalogue of tides as described in https://doi.org/10.1029/95GL03324. A number of constituents are stored in data/
    altimetry_mission: this is the satellite altimetry mission that is being studied. At the moment this includes jason-1, jason-2, jason-3, topex, envisat, ers-1 and ers-2. But ones own mission can be used by placing the length of one cycle in days in P=[ ]. 
    output: format for the outputting of the data 'array' or 'dataframe'
    cat_header: the header for catfile
    skip_rows_in_catfile: the number of rows to skip in catfile that is used
    P: ones own numbder of days used to study additional missions
    """
    import pandas as pd
    import numpy as np
    import xarray as xr
    
    con = constituent
    sk = skip_rows_in_catfile
    cat = pd.read_csv(catfile,header=[cat_header],delim_whitespace=True,
                 skiprows=[sk])
    # calling the catalogue of tidal constituents

    am = altimetry_mission
    
    if am == 'jason-1' or am == 'jason-2' or am == 'jason-3' or am == 'topex':
        P = 9.9156
        print('Cycle length = 9.9156 days')
    elif am == 'envisat' or am == 'ers-1' or am == 'ers-2':
        P = 35.0
        print('Cycle length = 35.0 days')
    else:
        if P > 0:
            P=P
            print('altimetry mission not implemented, using inserted cycle length')
        else:
            print('mission not included, please provide a cycle length')
            return

    alias_period = np.zeros((len(con)))
    
    # estimating tidal aliasing period

    for j in range(len(con)):
        
        ind = np.where(cat.DW==str(con[j]))[0]

        Tk = np.array(cat['freq'][ind])/360 *24
        fs = 1./P
        fk = Tk
        f_a = np.abs(np.mod(fk+fs/2,fs)-fs/2)
        alias_period[j] =  1/f_a

    alias_period[np.where(alias_period>10000)] = np.nan
    
    # outputting the data

    if output == None or output == 'array':
        return(alias_period)
    elif output == 'dataframe':
        print('Alias periods output into dataframe')
        a_period = pd.DataFrame(alias_period,columns=[str(am) + str(' aliasing period in days')],
                                index=constituent)
        return(a_period)
    else:
        print('file format not implemented, outputted in an array')
