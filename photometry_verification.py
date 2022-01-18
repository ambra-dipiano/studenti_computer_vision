import os
from os.path import isfile, expandvars
from sagsci.tools.utils import *
from sagsci.tools.photometry import *

# observation and target
obs_crab = 'data/bkg000001.fits'

target = {'ra': 33.557, 'dec': -51.841}
pointing = {'ra': 33.057, 'dec': -51.841}

# configuration
erange = [(0.03, 0.0449), (0.0449, 0.0671), (0.0671, 0.1003), (0.1003, 0.15)]
trange = [0, 10]         # livetime in seconds (s)
radius = 0.2               # photometry region in degrees (deg)
spectral_index = -2.1     # slope of the power-law spectrum
irf = expandvars('$CTOOLS/share/caldb/data/cta/prod3b/bcf/South_z40_average_LST_30m/irf_file.fits')

# we need to add "radius" to the target dictionary 
target['rad'] = radius

# init photometry
phm = Photometrics({'events_filename': obs_crab})

# remove duplicate files
offregionsfile = obs_crab.replace('.fits', '_off.reg')
if isfile(offregionsfile):
    os.remove(obs_crab.replace('.fits', '_off.reg'))
    
# compute regions
off_regions = phm.find_off_regions(algo='cross', src=target, pnt=pointing, rad=target['rad'], save=offregionsfile)    

for e in erange:
    print(f'Target = {target} TeV')
    print(f'Energy range = {e} s')
    print(f'Time range = {trange} deg')

    on, off, alpha, excess, sigma, err_note = phm.counting(src=target, rad=target['rad'], off_regions=off_regions, e_min=e[0], e_max=e[1], t_min=trange[0], t_max=trange[1], draconian=False)
    print(f'on counts = {on} cts')

    exposure = get_aeff_in_region(target=target, pointing=pointing, trange=trange, erange=e, irf=irf, index=spectral_index)
    print(f'aeff = {exposure} cm2')

    livetime = trange[1]-trange[0]
    print(f'livetime = {livetime} s')

    # compute flux 
    flux = on / exposure / livetime
    print(f'flux = {flux} ph/cm2/s')

    print(f'\n{"-"*50}\n')

