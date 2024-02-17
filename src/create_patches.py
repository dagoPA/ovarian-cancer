import h5py
import imageio
import numpy as np
from PIL.Image import Image

h5_example_path = '/data/UBC-OCEAN/TCGA-3C-AALI-01Z-00-DX1.F6E9A5DF-D8FB-45CF-B4BD-C6B76294C291.h5'
image_path = '/data/UBC-OCEAN/10077.png'

# open coords
with h5py.File(h5_example_path, 'r') as h5_example:
    # keep coords in variable
    coords = h5_example['coords'][:]

# Allow any pixel size
Image.MAX_IMAGE_PIXELS = None
# open the image
image = Image.open(image_path)
# convert image to array
image = np.array(image)

print('completed')
