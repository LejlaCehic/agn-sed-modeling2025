from astropy.io import fits
from astropy.table import Table
from astropy.coordinates import SkyCoord, match_coordinates_sky
import astropy.units as u
import pandas as pd
import numpy as np
from cigalePrepperV9_1 import cigalePrep
champs = pd.read_csv("agn_champs_matches_0.6arcsec.csv")
cosmos_path = 'C:/Users/lejla/AGN_Matching/COSMOSWeb_mastercatalog_v1.fits'
cosmos = fits.open(cosmos_path)
cosmos_phot   = Table.read(cosmos[1])
cosmos_lephare = Table.read(cosmos[2]) 
#CHAMPS: RA and DEC | COSMOS: ra and dec for COSMOS
champs_coords = SkyCoord(ra=champs     ['RA'].values * u.deg, dec=champs    ['DEC'].values * u.deg)
cosmos_coords = SkyCoord(ra=cosmos_phot['ra'].value * u.deg, dec=cosmos_phot['dec'].value * u.deg)
#perform matching: AGN (CHAMPS) to COSMOS
idx, d2d, _ = match_coordinates_sky(champs_coords, cosmos_coords)
max_sep = 0.6 * u.arcsec
mask = d2d < max_sep
#these are the AGN that matched
matched_champs = champs[mask]                     
matched_cosmos_phot = cosmos_phot[idx[mask]]          
matched_cosmos_lephare = cosmos_lephare[idx[mask]]   
#filter out redshifts
valid_z_mask = matched_cosmos_lephare['zfinal'] != -99
matched_champs = matched_champs[valid_z_mask]
matched_cosmos_phot = matched_cosmos_phot[valid_z_mask]
matched_cosmos_lephare = matched_cosmos_lephare[valid_z_mask]
cigalePrep(matched_cosmos_phot, matched_cosmos_lephare, "cigale_input_file.txt", ul=True)
