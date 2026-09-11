import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# automatically find the sample image in the folder
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = None
for file in os.listdir(script_dir):
    if file.lower().startswith('sample'):
        image_path = os.path.join(script_dir, file)
        break

if not image_path:
    raise FileNotFoundError("Could not find the sample image file in this folder!")

# load image and get original shape and memory
img = np.array(Image.open(image_path))
orig_shape = img.shape
orig_memory = img.nbytes

# step factor for downsampling
N = 8

# downsample image matrix using slicing (taking every N-th pixel)[cite: 1]
down_img = img[::N, ::N, :]
down_shape = down_img.shape
down_memory = down_img.nbytes

# re-expand back to original dimensions using np.repeat[cite: 1]
re_expanded = np.repeat(np.repeat(down_img, N, axis=0), N, axis=1)

# calculate reduction percentages
dim_reduction = (1 - (down_shape[0] / orig_shape[0])) * 100
memory_savings = (1 - (down_memory / orig_memory)) * 100

# print output matching the exact lab specification format
print(f"--- DOWNSAMPLING ANALYSIS (N = {N}) ---")
print(f"Original Shape : {orig_shape} | Memory: {orig_memory:,} bytes")
print(f"Downsampled Shape : {down_shape} | Memory: {down_memory:,} bytes")
print(f"Re-expanded Shape : {re_expanded.shape} | Visual: Blocky Pixelation")
print(f"Dimension Reduction: {dim_reduction:.2f}% reduction per axis")
print(f"Memory Savings : {memory_savings:.2f}% data reduction")

# display matplotlib figure output for task 4 checklist requirement
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].imshow(img)
axes[0].set_title("Original Image")
axes[0].axis('off')

axes[1].imshow(re_expanded)
axes[1].set_title(f"Re-expanded Image (N={N} - Blocky Pixelation)")
axes[1].axis('off')

plt.tight_layout()
plt.show()