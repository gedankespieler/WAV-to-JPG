import sys
import os
import math
from PIL import Image


with open('wav.wav', 'rb') as f:
    arr = f.read()

root = math.floor((len(arr) * (1/3)) ** (1/2))
size = (root, root)

im = Image.frombytes('RGB',size, arr)
im.save('image.jpg')
