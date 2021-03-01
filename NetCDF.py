import xarray as xr
import numpy as np


ds = xr.open_dataset('C:\Users\tadeu.didonet\Documents\Proj_Glinder_campanhas_01\campanha_18\pa0001au\pa0001au_001_200802_195117.nc')

#Convertendo as longitudes de 0 a 360 para -180 a 180

ds.coords['longitude'] = ((ds.coords['longitude'] + 180) % 360) - 180

dl = (((dlon) + 180) % 360) - 180
ds = ds.sortby(ds.longitude)

ds_subset = ds.sel(lonngitude=slice(-90, -20), latitude=slice(10, -60))
ds_subset


