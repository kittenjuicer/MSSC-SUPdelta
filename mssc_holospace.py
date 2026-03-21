from astropy.io import fits
cmb_map = fits.open('planck_cmb.fits')[1].data  # public file
local_holospace = project_weedeater_harmonics(accelerometer_data) + elliptic_ouroboros_closure(hollyhock_image)
coupled_psi = cmb_low_l_basis @ (local_holospace + history_kernel)
