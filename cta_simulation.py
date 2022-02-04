# *******************************************************************************
# Copyright (C) 2020-2021 INAF
#
# This software is distributed under the terms of the BSD-3-Clause license
#
# Authors:
# Ambra Di Piano <ambra.dipiano@inaf.it>
# *******************************************************************************

import ctools

def run_ctobssim(model, pointing, output, energy=(0.03, 150), time=(0, 10), fov=5, caldb='prod3b-v2', irf='South_z40_0.5h', seed=1):
    sim = ctools.ctobssim()
    sim["inmodel"] = model
    sim["outevents"] = output
    sim["caldb"] = caldb
    sim["irf"] = irf
    sim["ra"] = pointing[0]
    sim["dec"] = pointing[1]
    sim["rad"] = fov
    sim["tmin"] = time[0]
    sim["tmax"] = time[1]
    sim["emin"] = energy[0]
    sim["emax"] = energy[1]
    sim["seed"] = seed
    sim.execute()


def run_skymap(obs, output, energy=(0.03, 150), roi=5, caldb='prod3b-v2', irf='South_z40_0.5h', wbin=0.02):
    nbin = int(roi*2/wbin)
    skymap = ctools.ctskymap()
    skymap['inobs'] = obs
    skymap['outmap'] = output
    skymap['irf'] = irf
    skymap['caldb'] = caldb
    skymap['emin'] = energy[0]
    skymap['emax'] = energy[1]
    skymap['usepnt'] = True
    skymap['nxpix'] = nbin
    skymap['nypix'] = nbin
    skymap['binsz'] = wbin
    skymap['bkgsubtract'] = 'IRF'
    skymap['coordsys'] = 'CEL'
    skymap['proj'] = 'CAR'
    skymap.execute()

# definie the pointing and fov
pointing = (83.6331, 22.5145)
fov = 5

# define parameters
erange = (0.03, 5)     
trange = (0, 100) 
irf = 'North_z20_0.5h'

# simulate background
model = './models/bkg_irf.xml'
run_ctobssim(model=model, pointing=pointing, output='./data/bkg_test_sim.fits', energy=erange, time=trange, fov=fov, irf=irf)
run_skymap(obs='./data/bkg_test_sim.fits', output='./data/bkg_test_sky.fits', energy=erange, roi=fov, irf=irf)

# simulate source
model = './models/group4.xml'
run_ctobssim(model=model, pointing=pointing, output='./data/crab_test_sim.fits', energy=erange, time=trange, fov=fov, irf=irf)
run_skymap(obs='./data/crab_test_sim.fits', output='./data/crab_test_sky4_subIRF.fits', energy=erange, roi=fov, irf=irf)

