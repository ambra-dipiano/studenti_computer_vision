# *******************************************************************************
# Copyright (C) 2020-2021 INAF
#
# This software is distributed under the terms of the BSD-3-Clause license
#
# Authors:
# Ambra Di Piano <ambra.dipiano@inaf.it>
# *******************************************************************************

from sagsci.tools.plotting import SkyImage

# DL3 file
sky = './data/crab_test_sky4_subIRF.fits'

# params counts map
trange = [0, 100]
erange = [0.03, 150]
roi = 3
pixelsize = 0.02
target = {'ra': 83.6331, 'dec': 22.0145, 'rad': 0.2}
pointing = {'ra': 83.6331, 'dec': 22.5145}

# params plot
figsize = (5, 5)
fontsize = 10

# plot
plot = SkyImage()
img = sky.replace('.fits', '.png')
plot.set_pointing_from_dict(pointing=pointing)
plot.plot_fits_skymap(file=sky, name=img, figsize=figsize, fontsize=fontsize)
del plot
