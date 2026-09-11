import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Automatically find any file starting with 'sample' in the script folder
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = None
for file in os.listdir(script_dir):
    if file.lower().startswith('sample.'):
        image_path = os.path.join(script_dir, file)
        break

if not image_path:
    raise FileNotFoundError("No file starting with 'sample' was found in this folder!")

# Opening image and converting into numpy array
img = np.array(Image.open(image_path))

# Splitting the 3 channels (R, G, B) from axis 2
r_channel = img[:, :, 0]
g_channel = img[:, :, 1]
b_channel = img[:, :, 2]

print("--- CHANNEL EXTRACTION SUMMARY ---")
print(f"Original Image Shape: {img.shape}")
print(f"Red Channel 2D Shape: {r_channel.shape} | Mean Intensity: {r_channel.mean():.2f}")
print(f"Green Channel 2D Shape: {g_channel.shape} | Mean Intensity: {g_channel.mean():.2f}")
print(f"Blue Channel 2D Shape: {b_channel.shape} | Mean Intensity: {b_channel.mean():.2f}")

# Creating blank arrays to isolate each color channel
red_only = np.zeros_like(img)
red_only[:, :, 0] = r_channel

green_only = np.zeros_like(img)
green_only[:, :, 1] = g_channel

blue_only = np.zeros_like(img)
blue_only[:, :, 2] = b_channel

# Setting up 2x3 grid to plot color and grayscale maps
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Top row: color isolation
axes[0, 0].imshow(red_only)
axes[0, 0].set_title("Red-Only")
axes[0, 0].axis('off')

axes[0, 1].imshow(green_only)
axes[0, 1].set_title("Green-Only")
axes[0, 1].axis('off')

axes[0, 2].imshow(blue_only)
axes[0, 2].set_title("Blue-Only")
axes[0, 2].axis('off')

# Bottom row: grayscale intensity maps
axes[1, 0].imshow(r_channel, cmap='gray')
axes[1, 0].set_title("Red Grayscale")
axes[1, 0].axis('off')

axes[1, 1].imshow(g_channel, cmap='gray')
axes[1, 1].set_title("Green Grayscale")
axes[1, 1].axis('off')

axes[1, 2].imshow(b_channel, cmap='gray')
axes[1, 2].set_title("Blue Grayscale")
axes[1, 2].axis('off')

plt.tight_layout()
plt.show()