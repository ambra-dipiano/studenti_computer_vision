# *******************************************************************************
# Copyright (C) 2019-2021 INAF
#
# This software is distributed under the terms of the BSD-3-Clause license
#
# Authors:
# Ambra Di Piano <ambra.dipiano@inaf.it>
# *******************************************************************************

import os
from sagsci.tools.utils import *
from os.path import expandvars, isfile



# observation and source
obs_bkg = expandvars('./data/bkg_test_sim.fits')
obs_src = expandvars('./data/crab_test_sim.fits')
target = {'ra': 83.6331, 'dec': 22.0145}

# configuration
sigma = 5
erange = [0.03, 150]
trange = [0, 1200]
radius = 0.2
spectral_index = -2.48
target['rad'] = radius
irf = expandvars('$CTOOLS/share/caldb/data/cta/prod3b-v2/bcf/South_z40_0.5h/irf_file.fits')

# get poiting
pointing = get_obs_pointing(filename=obs_bkg)
print(f'pointing = {pointing} deg')

# find background counts in target region
regions = './data/bkg_regions.reg'
if isfile(regions):
    os.remove(regions)
bkg_counts_in_region = get_counts_in_region(filename=obs_bkg, target=target, pointing=pointing, trange=trange, erange=erange, off_regions=regions)
print(f'background counts = {bkg_counts_in_region} counts')

# get the excess from bkg and given sigma level
excess = get_excess_from_sigma_and_bkg(sigma=sigma, bkg=bkg_counts_in_region)
print(f'excess = {excess} counts')

# check to obtain the same sigma again
sigma = get_snr(signal=excess, bkg=bkg_counts_in_region)
print(f'snr = {sigma} sigmas')

# get exposure
exposure = get_exposure_in_region(target=target, pointing=pointing, trange=trange, erange=erange, irf=irf, index=spectral_index)
print(f'exposure = {exposure} cm2/s')

# compute flux 
flux = excess / exposure 
print(f'flux = {flux} ph/cm2/s')

# from flux find the prefactor of given spectral index
prefactor = get_prefactor(flux=flux, erange=erange, gamma=spectral_index, unit='TeV')
print(f'prefactor = {prefactor} ph/cm2/s/MeV')
