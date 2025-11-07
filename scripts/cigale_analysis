from astropy.table import Table
import matplotlib.pyplot as plt
import numpy as np

results = Table.read("C:/Users/lejla/AGN_Matching/cigale_run2/cigale_run2/out/results.fits")

redshifts = results["best.universe.redshift"]
clean_redshifts = redshifts[redshifts > 0]

# Sort the redshifts in ascending order and convert to list
sorted_redshifts = np.sort(clean_redshifts).tolist()

print(sorted_redshifts)
