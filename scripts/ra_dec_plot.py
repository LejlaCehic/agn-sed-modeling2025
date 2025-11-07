import matplotlib.pyplot as plt
#from astropy.table import Table
#from astropy.coordinates import SkyCoord, match_coordinates_sky
#import astropy.units as u
import pandas as pd

pointing_path = 'C:/Users/lejla/AGN_Matching/champs_calibrated_pointings.csv' 
pointings = pd.read_csv(pointing_path)

source = pd.read_csv("agn_champs_matches_1arcsec.csv") # overlapping catalog 

size = 8
fig = plt.figure(figsize=[10,7])
ax = fig.add_subplot(111)
plt.scatter(pointings.RA, pointings.DEC, s=10, marker= 'o',
            facecolors='none', edgecolor='gray',label='ALMA Pointings')
plt.scatter(source['RA'], source['DEC'],s=5,c='red',label='AGN Candidates')
plt.xlabel('RA',size=15)
plt.ylabel('DEC',size=15)
plt.legend()
plt.gca().invert_xaxis()
plt.show()
