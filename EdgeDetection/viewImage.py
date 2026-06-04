import torch
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt

#load the image
image = Image.open("fox.jpg").convert("L")
print("*********** PIL Image format ***************")
print(f"type(image) = {type(image)}, size = {image.size}")
print(f"image mode: {image.mode}")
