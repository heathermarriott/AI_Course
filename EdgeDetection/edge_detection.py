import torch
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt

# load the image
image = Image.open("fox.jpg").convert("L")
print("*********** PIL Image format ***************")
print(f"type(image) = {type(image)}, size = {image.size}")
print(f"image mode: {image.mode}")

# image to tensor
transform = transforms.ToTensor()
tensor = transform(image).unsqueeze(0) # add batch dim
print("*********** Tensor format ***************")
print(f"shape = {tensor.shape}")

kernel = torch.tensor(
    [[[[
2, 2, 2],
          [-1, -1, -1],
          [-1, -1, -1]]]],
    dtype=torch.float32  # convolutional kernel (filter)
)

edges = F.conv2d(tensor, kernel, padding=1)
edge_img = edges.squeeze().cpu().numpy()

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(image, cmap="gray")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Edges")
plt.imshow(edge_img, cmap="gray")
plt.axis("off")
