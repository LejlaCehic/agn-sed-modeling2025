# Analyzing Dusty AGN via Spectral Energy Distribution Modeling

This repository showcases my summer 2025 NSF-funded Research Experience for Undergraduates (REU) in Multimessenger Astrophysics at Rochester Institute of Technology (RIT). My project focused on identifying and modeling dusty active galactic nuclei (AGN) using spectral energy distribution (SED) fitting tools across multiwavelength data.

## Project Overview
-  Analyze high-redshift (z > 3) dusty AGN using photometric data from COSMOS, CHAMPS, and JWST surveys.
-  Python, NumPy, Pandas, Astropy, CIGALE
-  Utilized the RIT high-performance computing cluster to run CIGALE in batch mode, optimizing performance on large AGN datasets
-  Cross-matching AGN catalogs, filtering photometric redshifts, constructing input catalogs, and running SED models to estimate AGN properties.

## Data Sources
- **CHAMPS** – ALMA sub-mm photometry for dusty galaxy populations
- **COSMOS2020** – Deep optical/IR photometric catalogs
- **JWST/MIRI** – Mid-infrared imaging from COSMOS-Web

## Key Tasks
- Cleaned and cross-matched AGN candidates across multiple catalogs using RA/Dec positional matching
- Filtered galaxies based on redshift (z > 3), flux limits, and AGN likelihood
- Constructed `.fits` and `.csv` input files for CIGALE
- Ran SED fitting models with parameters such as `agn.frac` and `alpha` (Fritz2006)
- Analyzed outputs to understand dust-obscuration and AGN contributions

