import numpy as np
from PIL import Image

# Create a 3D numpy array of zeroes, then replace zeros with color
data = np.zeros((5, 4, 3), dtype=np.int8)
data[:] = [255, 255, 0]
data[:3] = [255,0,0]

img = Image.fromarray(data, mode='RGB')
img.save('canvas.png')
