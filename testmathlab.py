#python3

from astropy.stats import sigma_clipped_stats
from photutils import datasets
from photutils import DAOStarFinder
import time
import numpy as np
import tkinter
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from astropy.visualization import SqrtStretch
from astropy.visualization.mpl_normalize import ImageNormalize
from photutils import CircularAperture

matplotlib.use('Qt5Agg')
plt.ion()
fig, ax = plt.subplots()
ax.plot([1,2,3,4],[1,4,2,3])
plt.show(fig)






hdu = datasets.load_star_image()  
data = hdu.data[0:401, 0:401] 
print(data)
plt.imshow(data) 
time.sleep(5)
mean, median, std = sigma_clipped_stats(data, sigma=3.0)  
print((mean, median, std))  

daofind = DAOStarFinder(fwhm=3.0, threshold=5.*std)  
sources = daofind(data - median)  
for col in sources.colnames:  
    sources[col].info.format = '%.8g'  # for consistent table output
print(sources)  
positions = np.transpose((sources['xcentroid'], sources['ycentroid']))
apertures = CircularAperture(positions, r=4.)
norm = ImageNormalize(stretch=SqrtStretch())
plt.imshow(data, cmap='Greys', origin='lower', norm=norm, interpolation='nearest')
apertures.plot(color='blue', lw=1.5, alpha=0.5)

time.sleep(5)

