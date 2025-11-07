import matplotlib.pyplot as plt
from astropy.table import Table
from astropy.coordinates import SkyCoord, match_coordinates_sky
import astropy.units as u
import pandas as pd

#Read in the csv (pandas) and fits (astropy) files and convert to df 
cosmos_df = pd.read_csv("AGN_TK_ver06-03-25.csv")
champs_df = Table.read("champs_pybdsf_5sigma.fits").to_pandas()

cosmos_coords = SkyCoord(ra=cosmos_df['RA_mean'].values * u.degree, dec=cosmos_df['DEC_mean'].values * u.degree)
champs_coords = SkyCoord(ra=champs_df['RA'     ].values * u.degree, dec=champs_df['DEC'     ].values * u.degree)
idx, d2d, _ = match_coordinates_sky(cosmos_coords, champs_coords)

max_sep = d2d.arcsec < 0.6                                              # get to within 0.6 arcsec
agn_matches    = cosmos_df[max_sep].reset_index(drop=True)
champs_matches = champs_df.iloc[idx[max_sep]].reset_index(drop=True)

pointing_path = "C:/Users/lejla/AGN_Matching/champs_calibrated_pointings.csv"
pointings = pd.read_csv(pointing_path)

source = pd.read_csv("agn_champs_matches_0.6arcsec.csv") # your overlapping catalog here

#create image of COSMOS field with the AGN canidates
size = 8
fig = plt.figure(figsize=[10,7])
ax = fig.add_subplot(111)
plt.scatter(pointings.RA, pointings.DEC, s=10, marker= 'o',
            facecolors='none', edgecolor='gray',label='ALMA Pointings')
plt.scatter(source['RA'], source['DEC'],s=6,c='red',label='AGN Candidates')
plt.xlabel('RA',size=15)
plt.ylabel('DEC',size=15)
plt.title("AGN Candidates with ALMA Observations in the COSMOS Field", size=16) 
plt.legend()
plt.gca().invert_xaxis()
plt.show()

