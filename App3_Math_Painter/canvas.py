import numpy as np
from PIL import Image


class Canvas:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        self.data = np.zeros((height, width, 3), dtype=np.int8)
        self.data[:] = self.color

    def make(self, filename):
        img = Image.fromarray(self.data, mode='RGB')
        img.save(filename)
